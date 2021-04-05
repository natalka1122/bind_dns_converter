import os
import sys
import textfsm
import jinja2

READ_FILE = "bind-short.txt"
BIND_TEXTFSM_FILE = "bind-config.textfsm"

UNBOUND_JINJA = "unbound.jinja"
UNBOUND_BLOCKED_JINJA = "unbound-blocked.jinja"
UNBOUND_REDIRECT_JINJA = "unbound-redirect.jinja"

UNBOUND_FOLDER = "generated/unbound"
UNBOUND_BLOCK_FOLDER = "generated/unbound-blocked"
UNBOUND_REDIRECT_FOLDER = "generated/unbound-redirect"

NSD_MASTER_JINJA = "nsd-master.jinja"
NSD_SLAVE_JINJA = "nsd-slave.jinja"
NSD_CLEAN_JINJA = "nsd-clean.jinja"

NSD_MASTER_FOLDER = "generated/nsd-master"
NSD_SLAVE_FOLDER = "generated/nsd-slave"
NSD_BLOCK_FOLDER = "generated/nsd-blocked"

BLOCK_FILE = "db.empty"
REDIRECT_FILE = "block-sites.dns"

for folder in [
    UNBOUND_FOLDER,
#    UNBOUND_BLOCK_FOLDER,
#    UNBOUND_REDIRECT_FOLDER,
    NSD_MASTER_FOLDER,
    NSD_SLAVE_FOLDER,
#    NSD_BLOCK_FOLDER,
]:
    os.makedirs(folder, exist_ok=True)


bindconfig = open(READ_FILE, "r").read()
with open(BIND_TEXTFSM_FILE) as template:
    fsm = textfsm.TextFSM(template)
    parsed_bind = fsm.ParseText(bindconfig)

files_short_name = set()
file_full_name = set()

bind_dict = []
blocked_zones = []
redirect_zones = []
for zonename, zonetype, zonefile, masterip in parsed_bind:
    if zonetype == "hint":
        # That's a different option
        continue
    elif zonetype == "slave":
        # I do not need it
        continue
    elif zonetype != "master":
        print(
            f"zonename = {zonename}, zonetype = {zonetype}, zonefile = {zonefile} masterip = {masterip}"
        )
        print(f"Wrong zonetype")
        sys.exit(1)
    if len(masterip) > 0:
        print(
            f"zonename = {zonename}, zonetype = {zonetype}, zonefile = {zonefile} masterip = {masterip}"
        )
        print(f"len(masterip) = {len(masterip)}")
        sys.exit(1)

    file_short_name = os.path.basename(zonefile)
    zone = {"zonename": zonename, "zonefile": file_short_name}
    if file_short_name == BLOCK_FILE:
        blocked_zones.append(zone)
    elif file_short_name == REDIRECT_FILE:
        redirect_zones.append(zone)
    else:
        bind_dict.append(zone)
    files_short_name.add(file_short_name)
    file_full_name.add(zonefile)

if len(files_short_name) != len(file_full_name):
    print(
        f"Duplicate filenames. Handle with care. len(files_short_name) = {len(files_short_name)} len(file_full_name) = {len(file_full_name)}"
    )
print(f"One should copy these {len(files_short_name)} files:")
print("*" * 10)
print(files_short_name)
print("*" * 10)

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)

unbound = templateEnv.get_template(UNBOUND_JINJA)
unbound_blocked = templateEnv.get_template(UNBOUND_BLOCKED_JINJA)
unbound_redirect = templateEnv.get_template(UNBOUND_REDIRECT_JINJA)

nsd_master = templateEnv.get_template(NSD_MASTER_JINJA)
nsd_slave = templateEnv.get_template(NSD_SLAVE_JINJA)
nsd_blocked = templateEnv.get_template(NSD_CLEAN_JINJA)

for zone in bind_dict:
    nsd_master.stream(zones=[zone]).dump(
        os.path.join(NSD_MASTER_FOLDER, zone["zonename"] + ".conf")
    )
    nsd_slave.stream(zones=[zone]).dump(
        os.path.join(NSD_SLAVE_FOLDER, zone["zonename"] + ".conf")
    )
    unbound.stream(zones=[zone]).dump(
        os.path.join(UNBOUND_FOLDER, zone["zonename"] + ".conf")
    )

nsd_blocked.stream(zones=blocked_zones).dump(NSD_BLOCK_FOLDER + "_part1.conf")
unbound_blocked.stream(zones=blocked_zones).dump(UNBOUND_BLOCK_FOLDER + ".conf")

nsd_blocked.stream(zones=redirect_zones).dump(NSD_BLOCK_FOLDER + "_part2.conf")
unbound_redirect.stream(zones=redirect_zones).dump(UNBOUND_REDIRECT_FOLDER + ".conf")

# for zone in blocked_zones:
#     nsd_blocked.stream(zones=[zone]).dump(
#         os.path.join(NSD_BLOCK_FOLDER, zone["zonename"] + ".conf")
#     )
#     unbound_blocked.stream(zones=[zone]).dump(
#         os.path.join(UNBOUND_BLOCK_FOLDER, zone["zonename"] + ".conf")
#     )

# for zone in redirect_zones:
#     nsd_blocked.stream(zones=[zone]).dump(
#         os.path.join(NSD_BLOCK_FOLDER, zone["zonename"] + ".conf")
#     )
#     unbound_redirect.stream(zones=[zone]).dump(
#         os.path.join(UNBOUND_REDIRECT_FOLDER, zone["zonename"] + ".conf")
#     )
print("Finished")
print("*" * 10)

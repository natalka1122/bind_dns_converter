# $GENERATE 1-254 dialup$.dialup A 212.26.228.$
# $GENERATE 1-254 dialup$.dialup2 A 212.26.239.$
# $GENERATE 1-254 dialup$.dialup3 A 212.26.242.$

# for i in range(1,255):
#     print(f"dialup{i}.dialup A 212.26.228.{i}")

# for i in range(1,255):
#     print(f"dialup{i}.dialup2 A 212.26.239.{i}")

# for i in range(1,255):
#     print(f"dialup{i}.dialup3 A 212.26.242.{i}")

# # $GENERATE 1-31 $ PTR nat1-pppoe$.static.ryazan.ru.
# for i in range(1,32):
#     print(f"{i} PTR nat1-pppoe{i}.static.ryazan.ru.")

# # $GENERATE 33-63 $ PTR nat2-pppoe$.static.ryazan.ru.
# for i in range(33,64):
#     print(f"{i} PTR nat2-pppoe{i}.static.ryazan.ru.")

# # $GENERATE 65-95 $ PTR nat3-pppoe$.static.ryazan.ru.
# for i in range(65,96):
#     print(f"{i} PTR nat3-pppoe{i}.static.ryazan.ru.")

# # $GENERATE 97-127 $ PTR nat4-pppoe$.static.ryazan.ru.
# for i in range(96,128):
#     print(f"{i} PTR nat4-pppoe{i}.static.ryazan.ru.")

# # $GENERATE 129-159 $ PTR nat5-pppoe$.static.ryazan.ru.
# for i in range(129,160):
#     print(f"{i} PTR nat5-pppoe{i}.static.ryazan.ru.")

# # $GENERATE 161-191 $ PTR nat6-pppoe$.static.ryazan.ru.
# for i in range(161,192):
#     print(f"{i} PTR nat6-pppoe{i}.static.ryazan.ru.")

# # $GENERATE 193-223 $ PTR nat7-pppoe$.static.ryazan.ru.
# for i in range(193,224):
#     print(f"{i} PTR nat7-pppoe{i}.static.ryazan.ru.")

# # $GENERATE 225-254 $ PTR nat8-pppoe$.static.ryazan.ru.
# for i in range(225,255):
#     print(f"{i} PTR nat8-pppoe{i}.static.ryazan.ru.")

# $GENERATE 1-32 $ PTR nat1-sample$.static.ryazan.ru.
for i in range(1,31):
    print(f"{i} PTR nat1-sample{i}.static.ryazan.ru.")

# $GENERATE 33-47 $ PTR nat1-dialup$.static.ryazan.ru.
for i in range(33,48):
    print(f"{i} PTR nat1-dialup{i}.static.ryazan.ru.")

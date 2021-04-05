# bind_dns_converter

1. Put your data into jinja files
2. Get bind config with ```named-checkconf -p``` > bind-short.txt
3. Run ```python main.py```
4. There will be many files in ```generate``` folder. Use them as prefilled blocks of config

if your zone file contains $GENERATE - use ```generate.py``` as a reference to fix zone files

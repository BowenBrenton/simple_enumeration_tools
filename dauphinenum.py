import requests
import sys

sub_list = open("subdomains.txt").read()
subdomains = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        pass

    else:
        print("This could be a valid domain", sub_domains)
import requests
import sys

sub_list = open("yourdirectorylisthere.txt").read()
drct = sub_list.splitlines()

for dir in drct:
    dir_enum = f"http://{sys.argv[1]}/{dir}"
    r = requests.get(dir_enum)
    if r.status_code==404:
        pass
    else:
        print("This could be a valid directory", dir_enum)

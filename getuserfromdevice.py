import urllib.request
import json
import time
import argparse

parser = argparse.ArgumentParser(description='Get users logged in to users devices')
parser.add_argument('-i', '--ConnectId',
                    help='ID to get devices from', required=True)
options = parser.parse_args()

def get_connect_ids(device_id):
    url = "https://t13-staging.cptr.no/st/4/connect_user/" + device_id + "/devices?auth=[auth]"
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    cont = json.loads(r.decode('utf-8'))
    device_infos = cont["device_info"]
    usernames = []
    for device_info in device_infos:
        username = device_info["username"]
        usernames.append(username)
    print(usernames)
    return usernames

connect_id= str(options.ConnectId)

url = 'https://a0.cptr.no/st/4/connect_user/' + connect_id + '/info?key=KVEz-WDMsj&auth=[auth]&count=20000'
req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0
connect_ids = set()

##parcing json
for item in cont['devices']:
    counter += 1
    device_id = item.get("device_id")
    if device_id != 'fae886eb-0be9-471a-a174-6ea95a002f86':
        ids = get_connect_ids(device_id)
        connect_ids.update(ids)

print("Connect IDs: ", connect_ids)

print("Number of devices: ", counter)

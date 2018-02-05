import urllib.request
import json
import time

connect_id = input("connect_id: ")

url = 'https://a0.cptr.no/st/4/connect_user/' + connect_id + '/info?key=[auth_key]&count=20000'
req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0
total_size = 0

##parcing json
for item in cont['devices']:
    counter += 1
    #total_size += item['size']
    #print(total_)
    print(item['platform'], "device:", item['device_name'],"app version:",item['client_version'],"last connection:", time.asctime(time.localtime(int(item['last_connection'].split('.')[0]))))
    #print("Timestamp:", item['timestamp'], " Size:", humansize(item['size']))
    #print("----")

##print formated
#print (json.dumps(cont, indent=4, sort_keys=True))
print("Number of devices: ", counter)

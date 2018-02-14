import urllib.request
import json
import time

suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

connect_id = input("connect_id: ")

url = 'https://a0.cptr.no/st/4/connect_user/' + connect_id + '/files_info?key=[auth_key]&count=20000'
req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0
total_size = 0

##parcing json
for item in cont['files']:
    counter += 1
    total_size += item['size']
    #print(total_)
    print("Timestamp:", time.asctime(time.localtime(item['timestamp'])), " Size:", humansize(item['size']))
    #print("Timestamp:", item['timestamp'], " Size:", humansize(item['size']))
    #print("----")

##print formated
#print (json.dumps(cont, indent=4, sort_keys=True))
print("Number of files: ", counter, "Total Size: ",humansize(total_size))

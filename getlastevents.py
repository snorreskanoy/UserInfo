import urllib.request
import json
import time
import os.path
import sys
import argparse

#if __name__ == "__main__":
parser = argparse.ArgumentParser(description='Get latest actions from Capture storage')
parser.add_argument('-c', '--count',
                    help='Amout of actions to get (defaulu=100)', required=False, default=100)
options = parser.parse_args()

# Converting size view
suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    i = 0

    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

# Getting ConnectID to process
connect_id = input("connect_id: ")

url = 'https://a0.cptr.no/st/4/connect_user/' + connect_id + '/last_events?key=[auth_key]='+str(options.count)
req = urllib.request.Request(url)

# Parsing response setting defaults
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0
total_size = 0

# Unifying filetypes
def filetype(filename):
    filename = os.path.splitext(filename)[1][1:]

    if filename.lower() in ['jpg','jpeg','png','tif','gif']:
        filename='Image'
    elif filename.lower() in ['mp4','avi','flv','mpeg','mp4','hvec','mov']:
        filename='Video'
    else:
        filename == filename + ' not defined'
    return filename

# Parcing json printing last events
for item in cont['events']:
    counter += 1
    total_size += item['size']
    print(filetype(item['filename']), item['operation'], "on:", time.asctime(time.localtime(item['timestamp'])),"by:", item['computer_name'], "Size:", humansize(item['size']))
    #print("----")

# Printing total numbers for fetched data
print("Number of files: ", counter, "Total Size: ",humansize(total_size))

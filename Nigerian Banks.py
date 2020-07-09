import urllib.request, urllib.parse, urllib.error
import json
import ssl 

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = urllib.request.urlopen('https://nigerianbanks.xyz/', context = ctx)

data = url.read().decode()

info = json.loads(data)

dump_info = json.dumps(info, indent = 4)
# print (dump_info)
print (len(info))
count = 0
for bank in info :
    a = bank['logo']
    # print (a)
    count += 1
    image = urllib.request.urlopen(a).read()
    image_name = str(count)+'.jpg'
    f_handle = open(image_name, 'wb')
    f_handle.write(image)
    

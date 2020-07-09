import urllib.request, urllib.parse, urllib.error
import json
import ssl 

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = urllib.request.urlopen('https://nigerianbanks.xyz/', context = ctx)

bank_data = url.read().decode()

bank_json = json.loads(bank_data)

dump_json = json.dumps(bank_json, indent = 4)
print (dump_json)
print (len(bank_json))

for each_bank in bank_json :
    image_url = each_bank['logo']
    # print (a)
    image_url_list = image_url.split('/')
    # print (b)
    
    image = urllib.request.urlopen(image_url).read()
    image_name = image_url_list[4]
    f_handle = open(image_name, 'wb')
    f_handle.write(image)

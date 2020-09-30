import sqlite3
import ssl
import urllib.request
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service_url = 'https://swapi.dev/api/'
attribute = 'people'
url = urllib.request.urlopen(service_url+attribute, context = ctx)
read_url = url.read().decode()

json_url = json.loads(read_url)
data = json_url['results']

connection = sqlite3.connect('starwarsdb.sqlite')
cur = connection.cursor()
cur.execute('DROP TABLE IF EXISTS StarWars')
cur.execute('CREATE TABLE StarWars(name, height, mass, hair_color, skin_color, eye_color, birth_year, gender)')

for person in data:
    name = person['name']
    height = person["height"]
    mass = person['mass']
    hair_color = person['hair_color']
    skin_color = person['skin_color']
    eye_color = person['eye_color']
    birth_year = person['eye_color']
    gender = person['gender']

    cur.execute('''INSERT INTO StarWars(name, height, mass, hair_color, skin_color, eye_color, birth_year, gender)
                VALUES (?,?,?,?,?,?,?,?)''',(name, height, mass, hair_color, skin_color, eye_color, birth_year, gender))

    connection.commit()




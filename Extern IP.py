import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

html = urlopen(url)
data = json.load(html)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print('info about your extern IP\n')
print('IP: {4}\nRegion: {1}\nCountry: {2}\nCity: {3}\nOrganization: {0}'.format(org, region, country, city, ip))



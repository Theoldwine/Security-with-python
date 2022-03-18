from bs4 import BeautifulSoup

import requests

wsite = requests.get('https://www.climatempo.com.br/').content

soup = BeautifulSoup(wsite, 'html.parser')

#print(soup.prettify())

#weather = soup.find('span', class_='_margin-r-5')

#print(weather.string)

print(soup.title.string)

print(soup.a.string)

print(soup.p.string)
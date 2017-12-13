from bs4 import BeautifulSoup
import requests

URL_base = "https://www.linio.com.mx/search?q="

URI = "galaxy+s8"

URL = URL_base + URI

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

names = soup.find_all("a", {"class": "title-section"})[0:5]
prices = soup.find_all("span", {"class": "original-price"})[0:5]
images = soup.find_all("div", {"class": "image-container"})[0:5]

producto = dict()
lista = list()
'''for x in name:
    print (x.text)
for y in price:
    print (y.text)
for z in imagen:
	print (z.a.img["data-lazy"])'''

for x,y,z in zip(names,prices,images):
	producto["name"]=x.text
	producto["price"]=y.text
	producto["image"]=z.a.img["data-lazy"]
	lista.append(producto)
	producto=dict()

print(lista)



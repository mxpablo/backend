from bs4 import BeautifulSoup
import requests

URL_base = "https://www.linio.com.mx/search?q="

def busqueda2(URI):

	page = requests.get(URL_base + URI )

	soup = BeautifulSoup(page.content, 'html.parser')

	names = soup.find_all("a", {"class": "title-section"})[0:2]
	prices = soup.find_all("span", {"class": "original-price"})[0:2]
	images = soup.find_all("div", {"class": "image-container"})[0:2]

	producto = dict()
	lista = list()

	for x,y,z in zip(names,prices,images):
		producto["name"]=x.text
		producto["price"]=y.text
		producto["image"]=z.a.img["data-lazy"]
		lista.append(producto)
		producto=dict()
		print(lista)

busqueda2("tele")



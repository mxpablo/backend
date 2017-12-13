from bs4 import BeautifulSoup
import requests

URL_Base = "https://www.linio.com.mx/search?q="

def busqueda(URI):

	page = requests.get(URL_Base + URI)

	soup = BeautifulSoup(page.content, 'html.parser')

	names = soup.find_all("a", attrs= {"class": "title-section"})[0:5]
	prices = soup.find_all("span", attrs= {"class": "original-price"})[0:5]
	imagenes = soup.find_all("img", attrs={"class": "image-container"})[0:5]

	producto = dict()
	lista = list()

	print(names)

	for x,y,z in zip(names,prices,imagenes):
		producto["name"]=x.text
		producto["price"]=y.text
		producto["image"]=z.a.img["data-lazy"]
		lista.append(producto)
		producto=dict()

busqueda("tele")
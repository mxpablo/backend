from bs4 import BeautifulSoup
import requests

URL_Base = "https://www.linio.com.mx/search?q="

def busqueda(URI):

	page = requests.get(URL_Base + URI)

	soup = BeautifulSoup(page.content, 'html.parser')

	names = soup.find_all("a", {"class": "title-section"})[0:10]
	prices = soup.find_all("span", {"class": "original-price"})[0:10]
	imagenes = soup.find_all("div",{"class": "image-container"})[0:10]

	producto = dict()
	lista = list()

	for x,y,z in zip(names,prices,imagenes):
		producto["name"]=x.text
		p2 = y.text
		producto["prices"]=p2[1:][:-3]
		producto["url_image"]= "https:" + z.a.img["data-lazy"]
		lista.append(producto)
		producto=dict()

	return lista
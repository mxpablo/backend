from bs4 import BeautifulSoup
import requests

URL_Base = "https://www.liverpool.com.mx/tienda/?s="

def busqueda(URI):

	page = requests.get(URL_Base + URI)

	soup = BeautifulSoup(page.content, 'html.parser')

	names = soup.find_all("a", attrs= {"class": "product-name"})[0:10]
	prices = soup.find_all("span", attrs= {"class": "price-amount"})[0:10]
	imagenes = soup.find_all("img", attrs={"class": "product-thumb"})[0:10]

	producto = dict()
	lista = list()

	for name,price,imagen in zip(names,prices,imagenes):
		producto["name"] = name.span.text 
		p2 = price.text
		producto["prices"] = p2[:-2]
		producto["url_image"] = imagen["data-original"]
		lista.append(producto)
		producto = dict()

	return lista



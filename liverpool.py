from bs4 import BeautifulSoup
import requests

URL_Base = "https://www.liverpool.com.mx/tienda/?s="
URI = "samsung+s8"
URL = "https://www.liverpool.com.mx/tienda/?s=tele"


'''URL = URL_Base + URI'''

print(URL)

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

result_items = soup.find_all(class_ = 'item')
print(result_items)

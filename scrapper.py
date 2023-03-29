import requests
from bs4 import BeautifulSoup
# product code = input "Pota; had p
product_code = "96685108"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response=requests.get(url)
page=BeautifulSoup(response.text,'html.parser')
opinions=page.select("div.js_product-review")
print(len(opinions))
print(type(opinions))
#print(page.prettify())
for opinion in opinions:
    print(opinion)
    
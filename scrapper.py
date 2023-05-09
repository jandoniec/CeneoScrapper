import requests
from bs4 import BeautifulSoup
import json
import os

def get_element(ancestor,selector=None, atribute=None, return_list=False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector and atribute:
            return ancestor[atribute]
        if atribute:
            return ancestor.select_one(selector)[atribute].strip()
        return ancestor.select_one(selector).text.strip()
    except (AttributeError,TypeError):
        return None
selectors = {
    "opinion_id": [None, "data-entry-id"],
    "author": ["span.user-post__author-name"],
    "recommendation": ["span.user-post__author-recomendation > em"],
    "stars": ["span.user-post__score-count"],
    "purchased": ["div.review-pz"],
    "opinion_date": ["span.user-post__published > time:nth-child(1)","datetime"],
    "purchase_date": ["span.user-post__published > time:nth-child(2)","datetime"],
    "useful": ["button.vote-yes","data-total-vote"],
    "unuseful": ["button.vote-no","data-total-vote"],
    "content": ["div.user-post__text"],
    "cons": ["div.review-feature__title--negatives ~ div.review-feature__item", None, True],
    "pros": ["div.review-feature__title--positives ~ div.review-feature__item", None, True],
}


product_code = input("Podaj kod produktu: ")
page_no=1
all_opinions=[]
url = f"https://www.ceneo.pl/{product_code}/#tab=reviews"
while(url):
    print(url)
    response=requests.get(url)
    print(response.status_code)
    if response.status_code!=requests.codes.ok:
        page_no=None
        break
    page=BeautifulSoup(response.text,'html.parser')
#print("Test: ", get_element(page))
    opinions=page.select("div.js_product-review")
#print(len(opinions))
#print(type(opinions))
#print(page.prettify())

    for opinion in opinions:
        single_opinion={}
        for key,value in selectors.items():
            single_opinion[key]=get_element(opinion,*value)
        all_opinions.append(single_opinion)
    try:
        url="https://www.ceneo.pl/"+get_element(page, "a.pagination__next","href")
    except TypeError:
        url=None
print(len(all_opinions))

#39562616
#96685108
#105563156
#31260410
try:
    os.mkdir('./opinions')
except FileExistsError:
    pass

with open(f"./opinions/{product_code}.json","w",encoding="UTF-8") as jf:
    json.dump(all_opinions,jf,indent=4, ensure_ascii=False)

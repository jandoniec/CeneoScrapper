import requests
from bs4 import BeautifulSoup
import json

def get_element(ancestor,selector=None, atribute=None, return_list=False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector and atribute:
            return ancestor[atribute]
        if atribute:
            return ancestor.select_one(selector)[atribute].strip()
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None
selectors={
    "opinion_id":[None, "data-entry-id"],
    "author":["span.user-post__author-name"],
    "reccomendation":["span.user-post__author-recomendation"],
    "score":["span.user-post__score-count"],
    "purchased":["div.review-pz"],
    "published_at":["span.user-post__published > time:nth-child(1)","datetime"],
    "purchased_at":["span.user-post__published > time:nth-child(2)","datetime"],
    "thumbs_up":["span[id^=votes-yes]"],
    "thumbs_down":["span[id^=votes-no]"],
    "content":["div.user-post__text"],
    "pros": ["div.review-feature_col:has(›div.review-feature_title--positives)>div.review-feature_item",None,True],
    "cons": ["div.review-feature_col:has(›div.review-feature_title--negatives)>div.review-feature_item",None,True],
        
    }


# product code = input "Pota; had p
product_code = "96685108"
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
with open(f"./opinions/{product_code}.json","w",encoding="UTF-8") as jf:
    json.dump(all_opinions,jf,indent=4, ensure_ascii=False)

import requests
from bs4 import BeautifulSoup

def get_cos(selector, ancestor, selector, atribute=None, return_list=False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector:
            return ancestor[atribute]
        if atribute:
            return ancestor.select_one(selector)[atribute].strip()
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None


# product code = input "Pota; had p
product_code = "96685108"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response=requests.get(url)
page=BeautifulSoup(response.text,'html.parser')
opinions=page.select("div.js_product-review")
#print(len(opinions))
#print(type(opinions))
#print(page.prettify())
all_opinions=[]

for opinion in opinions:
    print(opinion["data-entry-id"])
    single_opinion={
        "opinion_id":opinion["data-entry-id"],
        "author":opinion.select_one("span.user-post__author-name").text.strip(),
        "reccomendation":opinion.select_one("span.user-post__author-recomendation").text.strip(),
        "score":opinion.select_one("span.user-post__score-count").text.strip(),
        "purchased":opinion.select_one("div.review-pz").text.strip(),
        "published_at":opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip(),
        "purchased_at":opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"].strip(),
        "thumbs_up":opinion.select_one("span[id^=votes-yes]").text.strip(),
        "thumbs_down":opinion.select_one("span[id^=votes-no]").text.strip(),
        "content":opinion.select_one("div.user-post__text").text.strip(),
        "pros": [pros.text.strip() for pros in opinion.select("div.review-feature_col:has(›div.review-feature_title--positives)>div.review-feature_item")],
        "cons": [cons.text.strip() for cons in opinion.select("div.review-feature_col:has(›div.review-feature_title--negatives)>div.review-feature_item")],
        
    }
all_opinions.append(single_opinion)
print(all_opinions)
# CeneoScrapper

# a
'''
for opinion in opinions:
    print(opinion["data-entry-id"])
    single_opinion={
        "opinion_id":get_element(opinion,None, "data-entry-id"),
        "author":get_element(opinion,"span.user-post__author-name"),
        "reccomendation":get_element(opinion,"span.user-post__author-recomendation"),
        "score":get_element(opinion,"span.user-post__score-count"),
        "purchased":get_element(opinion,"div.review-pz"),
        "published_at":get_element(opinion,"span.user-post__published > time:nth-child(1)","datetime"),
        "purchased_at":get_element(opinion,"span.user-post__published > time:nth-child(2)","datetime"),
        "thumbs_up":get_element(opinion,"span[id^=votes-yes]"),
        "thumbs_down":get_element(opinion,"span[id^=votes-no]"),
        "content":get_element(opinion,"div.user-post__text"),
        "pros": get_element(opinion, "div.review-feature_col:has(›div.review-feature_title--positives)>div.review-feature_item",None,True),
        "cons": get_element(opinion, "div.review-feature_col:has(›div.review-feature_title--negatives)>div.review-feature_item",None,True),
        
    }
    '''
import os
import pandas as pd
#import matplotlib

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")],sep="\n")

product_code = input("Podaj kod produktu: ")


opinions = pd.read_json(f"./opinions/{product_code}.json")

#print(opinions)

opinion_count=len(opinions.index)
opinion_count=opinions.shape[0]
pros_count=sum([False if len(p)==0 else True for p in opinions.pros])
cons_count=sum([False if len(p)==0 else True for p in opinions.cons])
pros_count=opinions.pros.map(lambda p: False if len(p)==0 else True).sum()
avg_score=opinions.cons.map(lambda c: False if len(c)==0 else True).sum()
print(pros_count)
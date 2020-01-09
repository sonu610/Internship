# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:35:38 2020

@author: spj20
"""

import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv",index_col=0)
print(reviews.rename(columns=dict(region_1='region', region_2='locale')))
#print(reviews.region)
print(reviews.rename_axis('wines', axis='rows'))

gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

combined_products = pd.concat([gaming_products, movie_products])

powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")

powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))
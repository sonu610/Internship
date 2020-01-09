# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:55:16 2020

@author: spj20
"""


import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv",index_col=0)

"""d1=reviews.groupby('points').price.min()
print(d1)

d2=reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
print(d2)

d3=reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
print(d3)

d4=reviews.groupby(['country']).price.agg([len, min, max])
print(d4)"""

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
"""print(countries_reviewed)

mi = countries_reviewed.index
type(mi)
print(mi)

print(countries_reviewed.reset_index())"""
countries_reviewed = countries_reviewed.reset_index()
"""print(countries_reviewed.sort_values(by='len'))
print(countries_reviewed.sort_values(by='len', ascending=False))
print(countries_reviewed.sort_index())

reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
print(reviews_written)
best_rating_per_price =  reviews.groupby('price').points.count()

best_rating_per_price =  reviews.groupby('price').points.max()
d=best_rating_per_price.sort_index()
print(d)


price_extremes =reviews.groupby('variety').price.agg([min,max])

#or price_extremes =reviews.groupby('variety')['price'].agg([min,max])

sorted_varieties=price_extremes.sort_values(by=['min', 'max'], ascending=False)

print(sorted_varieties)

reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()

print(reviewer_mean_ratings.describe())

country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)

print(country_variety_counts)"""





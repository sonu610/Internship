# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:05:32 2020

@author: spj20
"""

import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv",index_col=0)

data=reviews.country.describe()
print(data)

data1=reviews.points.mean()
print(data1)


data2=reviews.points.unique()

print(data2)


data3=reviews.country.unique()
print(data3)
data4=reviews.taster_name.value_counts()
print(data4)

review_points_mean = reviews.points.mean()
data5=reviews.points.map(lambda p: p - review_points_mean)
print(data5)
def remean_points(row):
    row.points = row.points - review_points_mean
    return row



data6=reviews.apply(remean_points, axis='columns')
print(data6)
print(reviews.country + " - " + reviews.region_1)

median_points = reviews.points.median()
reviews.country.unique()
reviews_per_country = reviews.country.value_counts()

centered_price =reviews.price- reviews.price.mean()


desc = reviews["description"]
print(desc) 

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

print(descriptor_counts)

def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')

print(star_ratings)




# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:52:04 2020

@author: spj20
"""

import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv",index_col=0)


print(reviews.region_2.fillna("Unknown"))

print(reviews.points.astype('float64'))
print(reviews.index.dtype)

print(reviews[pd.isnull(reviews.country)])

print(pd.isnull(reviews.price).sum())

point_strings = reviews.points.astype(str)

reviews_per_region = reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending=False)
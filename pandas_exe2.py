# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 23:31:17 2020

@author: spj20
"""
import pandas as pd

data = pd.read_csv("winemag-data-130k-v2.csv",index_col=0)
desc = data["description"]
print(desc) 

first_desc= data.description[0]
print(first_desc) 


first_row = data.iloc[0]
print(first_row)

print(desc.head(10))

indices = [1, 2, 3, 5, 8]
sample_data = data.loc[indices]

print(sample_data)

cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = data.loc[indices, cols]

print(df)
cols = ['country', 'variety']
df1 = data.loc[:99, cols]


print(df1)

top_oceania_wines = data.loc[
    (data.country.isin(['Australia', 'New Zealand']))
    & (data.points >= 95)
]





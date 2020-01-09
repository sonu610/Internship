# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:39:09 2020

@author: spj20
"""

import pandas as pd
print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B']))

fruits = pd.DataFrame([[30,21]],columns=["Apples","Bananas"])
fruit_sales = pd.DataFrame([[35,21],[41,34]],columns=["Apples","Bananas"],index=["2017 Sales","2018 Sales"])

ingredients = pd.Series(['4 cups','1 cup','2 large','1 can'], index=['Flour' , 'Milk', 'Eggs', 'Spam'], name='Dinner')

data = pd.read_csv("winemag-data_first150k.csv",index_col=0) 
# Preview the first 5 lines of the loaded data 
data.head()
print(data)

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
print(animals)

animals.to_csv("cows_and_goats.csv")

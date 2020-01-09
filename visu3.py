# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 13:32:12 2020

@author: spj20
"""

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

import seaborn as sns
print("Setup Complete")
ign_filepath='ign_scores.csv'
ign_data = pd.read_csv(ign_filepath, index_col="Platform", parse_dates=True)
"""print(ign_data)

plt.figure(figsize=(10,6))
sns.barplot(x=ign_data.index,y=ign_data['Racing'])# Your code here
plt.title("Average Score for Racing Games, by Platform")"""
plt.figure(figsize=(10,10))
sns.heatmap(ign_data,annot=True)

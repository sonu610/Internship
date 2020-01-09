# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 13:14:31 2020

@author: spj20
"""
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

import seaborn as sns
print("Setup Complete")
museum_filepath='museum_visitors.csv'
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)

plt.figure(figsize=(12,6))

#sns.lineplot(data=museum_data)
plt.title("Monthly Visitors to Avila Adobe")
sns.lineplot(data=museum_data['Avila Adobe'])
plt.xlabel("Date")
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:50:47 2020

@author: spj20
"""

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

import seaborn as sns
print("Setup Complete")
fifa_filepath = "fifa.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)
plt.figure(figsize=(16,6))

# Line chart showing how FIFA rankings evolved over time
sns.lineplot(data=fifa_data)
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:44:48 2020

@author: spj20
"""


import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

import seaborn as sns
print("Setup Complete")
candy_filepath='candy.csv'
candy_data = pd.read_csv(candy_filepath, index_col="id")

plt.figure(figsize=(10,6))
#sns.scatterplot(x=candy_data['sugarpercent'] , y=candy_data['winpercent'])

#sns.regplot(x=candy_data['sugarpercent'] , y=candy_data['winpercent'])
#sns.lmplot(x="pricepercent", y="winpercent", hue="chocolate", data=candy_data)

sns.swarmplot(x=candy_data['chocolate'] , y=candy_data['winpercent'])
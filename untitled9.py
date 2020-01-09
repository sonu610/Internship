# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:17:28 2020

@author: spj20
"""

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

import seaborn as sns
print("Setup Complete")
cancer_b_filepath = "cancer_b.csv"
cancer_m_filepath = "cancer_m.csv"
cancer_b_data = pd.read_csv(cancer_b_filepath,index_col="Id")

# Fill in the line below to read the (malignant) file into a variable cancer_m_data
cancer_m_data = pd.read_csv(cancer_m_filepath,index_col="Id")
plt.figure(figsize=(10,6))
sns.distplot(a=cancer_m_data['Area (mean)'] ,label="iris1",kde=False)
sns.distplot(a=cancer_b_data['Area (mean)'] ,label="iris2",kde=False)
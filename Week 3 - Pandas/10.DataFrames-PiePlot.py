# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:35:58 2021

@author: light
"""

# -*- coding: utf-8 -*-


# Import convention
import pandas as pd

# We will also need
import numpy as np
import matplotlib.pyplot as plt


"""
---------------
Working Example
---------------
"""
tipsData = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# Group by day and count rows per day
tipsData.groupby(['day']).count()

# Percentage of tips per day 
tipDayPercentage = 100 * tipsData.groupby(['day']).sum()['tip'] / tipsData.groupby(['day']).sum()['total_bill']

# Convert to dataframe
tipDayPercentage = tipDayPercentage.to_frame('tip(%)').reset_index()

# Pie plot
days = pd.DataFrame(tipsData['day'].value_counts())
days.reset_index(inplace=True)
fig, ax = plt.subplots()
days.plot(kind='pie',y='day',labels=days['index'],autopct='%1.2f', ax=ax)
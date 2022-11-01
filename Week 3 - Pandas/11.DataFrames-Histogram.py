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

# Histogram
fig, ax = plt.subplots(1,2)
tipsData.hist(column='total_bill', ax=ax[0])
tipsData.hist(column='total_bill', bins = 100, ax=ax[1])
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:35:06 2021

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
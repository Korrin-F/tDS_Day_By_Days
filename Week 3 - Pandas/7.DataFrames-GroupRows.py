# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:34:02 2021

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
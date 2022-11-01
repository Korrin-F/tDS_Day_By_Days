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

tipsData.describe()

# Check if missing values
tipsData.isnull().sum()
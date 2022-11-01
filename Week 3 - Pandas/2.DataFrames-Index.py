# -*- coding: utf-8 -*-


# Import convention
import pandas as pd

# We will also need
import numpy as np
import matplotlib.pyplot as plt


"""
----------
DataFrames
----------
"""

df = pd.DataFrame(
        [[1,4,7],
         [2,5,8],
         [3,6,9]],
        index = [1,2,3],
        columns = ['a','b','c'])

# Indexing
print()
print("Let the DataFrame df = ")
print(df)
print()
print("df.loc[1,'c'] or df.iloc[0,2] is ")
print(df.iloc[0,2])
print()
print("df.loc[2,['b','c']] or df.iloc[1,1:3] is ")
print(df.iloc[1,1:3])
print()
print("df.loc[:,'a'] or df.iloc[:,0] is ")
print(df.iloc[:,0])
print()

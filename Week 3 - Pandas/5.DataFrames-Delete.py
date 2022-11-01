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

# Delete
print()
print("Delete column 'c'")
print(df.drop(columns='c'))
print()
print("Delete rows 1 and 3")
print(df.drop([1,3]))
print()

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

# Sort
print()
print("Sort rows based on column 'a' (descending) ")
print(df.sort_values('a', ascending=False))
print()
print("Sort columns based on row 1 (descending) ")
print(df.sort_values(1, axis=1, ascending=False))
print()

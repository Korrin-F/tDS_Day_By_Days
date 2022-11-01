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

# Append
print()
print("df.concat([df,df], axis=1) appends columns ")
print(pd.concat([df,df], axis=1))
print()
print("df.concat([df,df]) appends rows ")
print(pd.concat([df,df]))
print()

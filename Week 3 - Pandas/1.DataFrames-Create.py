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

# Creating
df = pd.DataFrame(
        {"a": [1,2,3],
         "b": [4,5,6],
         "c": [7,8,9]},
        index = [1,2,3])

df = pd.DataFrame(
        [[1,4,7],
         [2,5,8],
         [3,6,9]],
        index = [1,2,3],
        columns = ['a','b','c'])

dfMultiIndex = pd.DataFrame(
        {"a": [1,2,3],
         "b": [4,5,6],
         "c": [7,8,9]},
        index = pd.MultiIndex.from_tuples(
                [('d',1),('d',2),('e',2)],
                names = ['x1','x2']))
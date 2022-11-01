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

# Append
print()
print("df.concat([df,df], axis=1) appends columns ")
print(pd.concat([df,df], axis=1))
print()
print("df.concat([df,df]) appends rows ")
print(pd.concat([df,df]))
print()

# Sort
print()
print("Sort rows based on column 'a' (descending) ")
print(df.sort_values('a', ascending=False))
print()
print("Sort columns based on row 1 (descending) ")
print(df.sort_values(1, axis=1, ascending=False))
print()

# Delete
print()
print("Delete column 'c'")
print(df.drop(columns='c'))
print()
print("Delete rows 1 and 3")
print(df.drop([1,3]))
print()


"""
---------------
Working Example
---------------
"""
tipsData = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

tipsData.describe()

# Check if missing values
tipsData.isnull().sum()

# Group by day and count rows per day
tipsData.groupby(['day']).count()

# Percentage of tips per day 
tipDayPercentage = 100 * tipsData.groupby(['day']).sum()['tip'] / tipsData.groupby(['day']).sum()['total_bill']

# Convert to dataframe
tipDayPercentage = tipDayPercentage.to_frame('tip(%)').reset_index()

# Bar plot
fig, ax = plt.subplots()
tipDayPercentage.plot(kind='bar', x='day', y='tip(%)', color='red', ax=ax)

# Pie plot
days = pd.DataFrame(tipsData['day'].value_counts())
days.reset_index(inplace=True)
fig, ax = plt.subplots()
days.plot(kind='pie',y='day',labels=days['index'],autopct='%1.2f', ax=ax)

# Histogram
fig, ax = plt.subplots(1,2)
tipsData.hist(column='total_bill', ax=ax[0])
tipsData.hist(column='total_bill', bins = 100, ax=ax[1])

# Pivot table
table = pd.DataFrame(pd.pivot_table(tipsData,index=['sex','smoker'],aggfunc=np.sum)['total_bill'])
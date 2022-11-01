import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('car_data.csv')  # load our data

# select the 2nd and 3rd columns and convert them to a numpy array
X = data.iloc[:, 2].values.reshape(-1, 1)
Y = data.iloc[:, 6].values.reshape(-1, 1)

linear_regressor = LinearRegression()  # create a linear regression object
linear_regressor.fit(X, Y)  # perform the linear regression
Y_pred = linear_regressor.predict(X)  # make the predictions based on the model

# plotting data and predicted variable
plt.scatter(X, Y)
plt.plot(X, Y_pred, color='green')
plt.xlabel('Selling price')
plt.ylabel('Max power') 
plt.show()
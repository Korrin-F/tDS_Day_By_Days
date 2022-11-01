import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

data = pd.read_csv('candy-data.csv') # load our data

X = data.iloc[:, [3,12]].values
y = data.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

scaler_X = StandardScaler()
X_train = scaler_X.fit_transform(X_train) # Scaling  training set
X_test = scaler_X.transform(X_test) # Scaling test set

logisticRegression_model = LogisticRegression(random_state=0) # Logistic Regression model
logisticRegression_model.fit(X_train, y_train) # Training the model

prediction = logisticRegression_model.predict(X_test) # Predict the response

confusion_matrix = confusion_matrix(y_test, prediction) # Create a confusion matrix
print("Accuracy:", (confusion_matrix[0][0] + confusion_matrix[1][1]) / 22) # Checking LR accuracy
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics, svm


# Prepare the data
data = pd.read_csv('fruit_types.csv')
X = data.iloc[:,2:5]
Y = data.iloc[:,0]

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3,random_state=99)

# Define kernels and meassure the accuracy
kernels = ['linear', 'rbf', 'sigmoid']
accKernels = np.zeros(len(kernels))

for i, kernel_name in enumerate(kernels):
    clf = svm.SVC(kernel=kernel_name)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accKernels[i] = metrics.accuracy_score(y_test, y_pred)
    
    
# Define degrees for the polynomial kernel
p = X_train.shape
p = p[1]
degrees = [p, p+1, p+2, p+3, p+4, p+5]
accPoly = np.zeros(len(degrees))

for i in degrees:
    clf = svm.SVC(kernel='poly')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accPoly[i] = metrics.accuracy_score(y_test, y_pred)

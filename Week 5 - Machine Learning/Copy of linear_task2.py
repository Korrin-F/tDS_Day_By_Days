import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

data = pd.read_csv('uni_data.csv')  # load our data

X = data.iloc[:-1, 3:6] # set predicting variables
y = data.iloc[:-1, 9] # set variable to predict (score)

# define models
model_lasso = Lasso(alpha=0.01)
model_ridge = Ridge(alpha=0.01)

# fit models
model_lasso.fit(X, y)
model_ridge.fit(X, y)

# define new data to predict
new = data.iloc[2199, 3:6]

# make predictions
prediction_lasso = model_lasso.predict([new])
prediction_ridge = model_ridge.predict([new])

# summarize predictions
print('Predicted: %.3f' % prediction_lasso)
print('Predicted: %.3f' % prediction_ridge)






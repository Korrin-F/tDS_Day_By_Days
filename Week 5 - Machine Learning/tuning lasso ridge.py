import numpy as np
import pandas as pd
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import RepeatedKFold

data = pd.read_csv('uni_data.csv')  # load our data

X = data.iloc[:-1, 1:9] # set predicting variables
y = data.iloc[:-1, 9] # set variable to predict (score)

# define model evaluation method
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)

# define model
model = RidgeCV(alphas=np.arange(0.5, 1, 0.01), cv=cv, scoring='neg_mean_absolute_error')

# fit model
model.fit(X, y)

# summarize chosen configuration
print('alpha: %f' % model.alpha_)








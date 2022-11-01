import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_csv('food_data.csv')  # load our data

data.index = data.iloc[:,0] # Name rows as food for reference
data_to_use = data.iloc[:,3:15]
data_to_target = data.iloc[:,16]

X_train, X_test, y_train, y_test = train_test_split(data_to_use, data_to_target, test_size=0.3, random_state=21) # 70% training, 30% test

gaussian_model = GaussianNB() # Gaussian model

gaussian_model.fit(X_train, y_train) # Training the model

prediction = gaussian_model.predict(X_test) # Predict the response

result = {'food_type':y_test, 'pred':prediction}
result_df = pd.DataFrame(result)

print("Accuracy:", metrics.accuracy_score(y_test, prediction)) # Checking NB accuracy

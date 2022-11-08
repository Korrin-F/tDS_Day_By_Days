# some popular deployment apps
# heroku
# streamlit (simple)

# import some packages 
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# import the dataset
df = pd.read_csv('/Users/Korrin/Library/Mobile Documents/com~apple~CloudDocs/Learning & Books/the_Developer_Academy/Repositories/Day_by_Days/Week 6 - Knn_DecisionTree_SVM/diabetes.csv')

# set headings for the app
st.title('Diabetes Prediction App')
st.sidebar.header('User Input Parameters')
st.subheader('Data Information:') # will show the mean, median, max and min values of the dataset
st.write(df.describe()) # will show the dataset inside the subheader 

# setting my dependent and independent variables
# X = df.iloc[:, 0:8].values
X = df.drop(['Outcome'], axis=1) # this is another way to write it it means use all columns except the outcome column
y = df.iloc[:, -1].values

# splitting the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# creating a function to get user input
def user_report():
    # this creates a slider for the user to slide to a chosen value
    # this is the numbers that we will assign to variables, the text is what the user sees. The numbers are (min, max, default) which we can get from the dataset
    p = st.sidebar.slider('Pregnancies', 0, 17, 3) 
    g = st.sidebar.slider('Glucose', 0, 199, 117) 
    bp = st.sidebar.slider('Blood Pressure', 0, 122, 72) 
    skinT = st.sidebar.slider('Skin Thickness', 0, 99, 23) 
    insulin = st.sidebar.slider('Insulin', 0.0, 846.0, 30.5) 
    bmi = st.sidebar.slider('BMI', 0.0, 67.1, 32.0) 
    dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.078, 2.42, 0.3725) 
    age = st.sidebar.slider('Age', 21, 90, 29) 
    # the user input will be stored in a variable dictonary
    # these are the columns in the dataset so they need to match the names exactly 
    user_report_data = {
        'Pregnancies': p,
        'Glucose': g,
        'BloodPressure': bp,
        'SkinThickness': skinT,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': dpf,
        'Age': age
    }
    # convert the user input dictionary into a dataframe
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

# Patient data
user_data = user_report() # this is the variable that will store the user input
st.header('Patient Data')
st.write(user_data)

# Model trianing
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=13)
knn.fit(X_train, y_train)
user_result = knn.predict(user_data) 

# Model testing
y_pred = knn.predict(X_test)


# output
st.header('Your diabetes report: ')
output = ''
if user_result[0] == 0:
    output = 'You do not have diabetes'
else:
    output = 'You have diabetes'
st.title(output)
st.subheader('Accuracy Score: ')
st.write(str(accuracy_score(y_test, y_pred)*100)+'%')

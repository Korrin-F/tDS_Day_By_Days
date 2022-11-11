# --------------------------------------------
# Imorting
# --------------------------------------------

import numpy as np
import pandas as pd
import streamlit as st
import streamlit_echarts as st_echarts
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# import the datasets
train_data = pd.read_csv('new_train_data.csv')
test_data = pd.read_csv('new_test_data.csv')
combined_data = pd.read_csv('new_combined_data.csv')

# --------------------------------------------
# Creating the app details
# --------------------------------------------

# MAIN PAGE
st.title('Titanic Survival Prediction App')

# SIDEBAR
st.sidebar.image('titanic.png', width=300)
st.sidebar.header('Parameters:')
st.sidebar.subheader('Please enter your details below to see if you would have survived the Titanic')

# --------------------------------------------
# User input
# --------------------------------------------

# SIDEBAR
def user_input():
    def normalize_data(data, max_value):
        norm_data =  data/max_value 
        return norm_data
    # AGE
    age = st.sidebar.slider('What is your age?', 0, 80, 29)
    max_age = 80
    norm_age = normalize_data(age, max_age)
    # IS FEMALE & IS MALE 
    g = st.sidebar.radio('Are you male or female?', ['Male','Female'])
    gF = 0
    gM = 0
    match g:
        case 'Male':
            gM = 1
            gF = 0
        case 'Female':
            gM = 0
            gF = 1
        case _:
            gM = 1
            gF = 0
    # ALONE 
    a = st.sidebar.radio('Are you with family or traveling alone?', ['With family', 'Alone'])
    match a:
        case 'With Family':
            a = 0
        case 'Alone':
            a = 1
        case _:
            a = 1
    # SOUTHAMPTON & QUEENSTOWN & CHERBOURG
    p = st.sidebar.radio('Which port did you embark from?', ['Southampton', 'Queenstown', 'Cherbourg'])
    pS = 0
    pQ = 0
    pC = 0
    match p:
        case 'Southampton':
            pS = 1
            pQ = 0
            pC = 0
        case 'Queenstown':
            pS = 0
            pQ = 1
            pC = 0
        case 'Cherbourg':
            pS = 0
            pQ = 0
            pC = 1
        case _:
            pS = 1
            pQ = 0
            pC = 0
    # FIRST CLASS & SECOND CLASS & THIRD CLASS
    c = st.sidebar.radio('Which class did you travel in?', ['First Class', 'Second Class', 'Third Class'])
    c1 = 0
    c2 = 0
    c3 = 0
    match c:
        case 'First Class':
            c1 = 1
            c2 = 0
            c3 = 0
        case 'Second Class':
            c1 = 0
            c2 = 1
            c3 = 0
        case 'Third Class':
            c1 = 0
            c2 = 0
            c3 = 1
        case _:
            c1 = 0
            c2 = 0
            c3 = 1
    # FARE
    f = st.sidebar.slider('How much did you pay for your ticket?', 0.0, 512.0, 33.0)
    max_f = 512.0
    norm_f = normalize_data(f, max_f)

    # DATAFRAME
    user_input_dic = {
        'Alone': a,
        'is Female': gF,
        'is Male': gM,
        'Southampton': pS,
        'Cherbourg': pC,
        'Queenstown': pQ,
        'First Class': c1,
        'Second Class': c2,
        'Third Class': c3,
        'Norm_Age': norm_age,
        'Norm_Fare': norm_f  
    }
    user_input_df = pd.DataFrame(user_input_dic, index=[0])
    return user_input_df

# --------------------------------------------
# Store and Display the user input
# --------------------------------------------
user_data = user_input()

st.header('Your profile:')
st.write(user_data)

# --------------------------------------------
# Creating the model
# --------------------------------------------
# TRAINING DATA
X_train = train_data.drop(['Survived'], axis=1)
X_test = test_data.drop(['Survived'], axis=1)

y_train = train_data['Survived']
y_test = test_data['Survived']  

classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# PREDICTION with User's Data
user_result = classifier.predict(user_data)
Y_pred = classifier.predict(X_test)

#---------------------------------------------
# Display the results
#---------------------------------------------
st.header('Results:')

# ACCURACY
accuracy = accuracy_score(y_test, Y_pred)
accuracy_perc = str(round(accuracy*100)) + '%'

if user_result == 1:
    output = ' died. 😬 Sorry.'
elif user_result == 0:
    output = ' survived. 🥳 Congratulations!'
else:
    output = ' some thing has gone wrong. 😬 Oops.'

st.subheader('I am ' + accuracy_perc + '  sure that you will have' + output)

# CHARTS
options = {
    "xAxis": {
        "type": "category",
        "data": ["Male", "Female", "Family", "Alone", "First Class", "Second Class", "Third Class", "Southampton", "Queenstown", "Cherbourg"],
        'splitNumber': 10,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": [
                {"value": 13, "itemStyle": {"color": "#225273"}},# male survival percentage
                {"value": 83, "itemStyle": {"color": "#225273"}},# female survival percentage
                {"value": 51, "itemStyle": {"color": "#369d9e"}}, # family survival percentage
                {"value": 29, "itemStyle": {"color": "#369d9e"}}, # alone survival percentage
                {"value": 58, "itemStyle": {"color": "#55c595"}}, # First Class survival percentage
                {"value": 42, "itemStyle": {"color": "#55c595"}}, # Second Class survival percentage
                {"value": 27, "itemStyle": {"color": "#55c595"}}, # Third Class survival percentage
                {"value": 33, "itemStyle": {"color": "#7ce496"}}, # Southampton survival percentage
                {"value": 44, "itemStyle": {"color": "#7ce496"}}, # Queenstown survival percentage
                {"value": 49, "itemStyle": {"color": "#7ce496"}}, # Cherbourg survival percentage

            ],
            "type": "bar",
        }
    ],
}
# this next line was originally just st_echarts(...) but the object was not callable adding st_echarts.st_echarts(...) fixed the issue
st_echarts.st_echarts( 
    options=options,
    height="500px",
    width="100%",
)
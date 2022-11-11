# Week 6 - tDA Assignment
### Titanic Dataset 
---

Aim: Analyse the titanic dataset and create a survival prediction using logistic regression. Finally, deploy the model using Streamlit and build a user interface to adjust the parameters and see the outcome. 

---
### Workflow and Associated Files
Starting here...
Step 1: combined_data.ipynb 
    In this file, I have combined the three data sets provided back into one document. I did a bit of cleaning but the main purpose was to visualise and compare some of the columns to better understand the data. There is a conclusion section at the bottom. 
Step 2: train_test.ipynb
    In this file, I clean the data properly by dealing with Null values and converting the data to between 0-1. I then train and run a logistic regression model. The accuracy of the model has claimed to be at about 96%. From here I save the converted data into two new files that I will use in the deployment app. 
Step 3: app_titanic.py + new_test_data.csv + new_train_data.csv
    In this step, I fill out a simple user interface using Streamlit that will allow me to capture user data. The data is then converted into the integers required for the model to perform well and the results are displayed. 

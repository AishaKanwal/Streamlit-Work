import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score



#make containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Kashti Dataset ki App")
    st.text("In this project, we will work on kashti data")

with data_sets:
    st.header("Kashti doob gai, Haaaaww!")
    st.text("We will work with titanic dataset")
    #import data
    df = sns.load_dataset('titanic')
    st.write(df)
    df = df.dropna()
    st.write(df.head(10))

    st.subheader("Sambha, Ary o Sambha! Kitnay Aadmi thy?")
    st.bar_chart(df['sex'].value_counts())

    #other plot
    st.subheader("Class k hisab se farak")
    st.bar_chart(df['class'].value_counts())

    #barplot
    st.bar_chart(df['age'].sample(15)) #or head(15)

with features:
    st.header("There are our app features:") 
    st.text("Awein bht sare features add krty hain. asaan hi hay")
    st.markdown('1. **Feature 1:** This will tell us ___________________')
    st.markdown('2. **Feature 2:** This will tell us ___________________')
    st.markdown('3. **Feature 3:** This will tell us ___________________')

with model_training:
    st.header("Kashti walon ka kia bana?")
    st.text("ہم اپنے ڈیٹا سیٹ میں اضافہ یا کمی کریں گے۔")
    #making columns 
    input, display = st.columns(2)
    #pahle column main ap k selection points ho 
    max_depth = input.slider("How many people do you know?", min_value=10, max_value=100, value=20, step=5)

# n_estimator
n_estimators = input.selectbox("How many tree should be there in a RF?", options=[50,100,200,300,'No limit'])

#adding list of features
input.write(df.columns)

#input features from user
input_features = input.text_input('Which feature we should use?')

# machine learning model
model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
# yahan p hum aik condition lagayen gay
if n_estimators == 'No limit':
        model = RandomForestRegressor(max_depth = max_depth)
else:
        model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

#define x and y
M = df[[input_features]]
n = df[['fare']]

#fit our model
model.fit(M, n)
pred = model.predict(n)

#Display metrices
display.subheader("Mean absolute error of the model is: ")
display.write(mean_absolute_error(n, pred))
display.subheader("Mean squared error of the model is: ")
display.write(mean_squared_error(n, pred))
display.subheader("R squared error of the model is: ")
display.write(r2_score(n, pred))
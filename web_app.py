# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as snscconda
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# heading of the app
st.write("""
# Explore different ML models and darasets
Let's see which one is best among the following ML models: """)

# dataset k name ak box daal k sidebar py laga do
dataset_name = st.sidebar.selection(
    'select dataset',
    ('Iris', 'Breast Cancer', 'Wine')
)

# or isi k nichy classifier k nam ik dabay m dal do
classifier_name = st.sidebar.selection(
    'select classifier',
    ('KNN', 'SVM', 'Random Forest')
)
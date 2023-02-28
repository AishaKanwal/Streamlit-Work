import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Webapp title
# '''  '''  triple string hum multiple line of codes in a single quote k lye use krty hain.
st.markdown(''' 
# **Exploratory Data Analysis (EDA) Web Application**
This app is developed by AishaKanwal called **EDA APP**''')

# How to upload a file from pc

with st.sidebar.header(" Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset('titanic')
    # st.sidebar.markdown("[Example CSV file](https://raw.githubusercontent.com/aishakanwal/eda-app/master/titanic.csv)")
    st.sidebar.markdown("[Example CSV file](https://github.com/codeforamerica/ohana-api/blob/master/data/sample-csv/addresses.csv)")
#profiling report for pandas
if uploaded_file is not None:
    @st.cache #speedup dataframe loading, jb b hum koi b variable or data dengy 
    #toh wo ik e br m save krdega toh usko next time ziada time nh lagega 
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('----')
    st.header('**Profile Report with Pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for your file (csv)')
    if st.button('Press to use example data'):
    #example dataset
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.randn(100, 5),
                            columns=['Age', 'Height', 'weight', 'BMI', 'Total_score'])
            return a
        df = load_data()                     
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('----')
        st.header('**Profile Report with Pandas**')
        st_profile_report(pr)
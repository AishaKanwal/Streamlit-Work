import streamlit as st
import seaborn as sns

st.header("This video is brought to you by Aisha Kanwal")
st.text("Enjoying using streamlit?")
st.header("Wait is over. Boooooooom!")

df = sns.load_dataset('iris')
st.write(df.head(2))
st.write(df[['species', 'sepal_length', 'petal_length']].head(10))
st.bar_chart(df['sepal_length'])
st.line_chart(df['sepal_length'])

st.header("Yahoooooooooooooooo!! it is working fine :-D")



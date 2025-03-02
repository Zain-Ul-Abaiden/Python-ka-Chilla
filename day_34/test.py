import streamlit as st
import seaborn as sns

st.header("This video is brought to you by Streamlit")
st.text("This is a test")

st.header("Iris Dataset")
st.text("Iris dataset is a dataset that contains the measurements of iris flowers.")

df = sns.load_dataset("iris")
st.write(df[['species', 'sepal_length', 'petal_length']].head(10))

st.bar_chart(df['sepal_length'])
st.line_chart(df['sepal_length'])
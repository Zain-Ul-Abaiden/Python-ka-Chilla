import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport  # Updated import
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns

# Webapp Title
st.markdown('''
# **Exploratory Data Analysis Web Application**
This web application is designed to perform exploratory data analysis (EDA) on a given dataset.
It provides various functionalities to visualize and analyze the data.
''')

# Upload a file from PC
with st.sidebar.header('Upload Dataset (.csv)'):
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    st.sidebar.markdown(
        'Example CSV file: [Click here](https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv)',
        unsafe_allow_html=True
    )

# Load dataset function
@st.cache_data
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

# Create profiling report function
@st.cache_data
def create_report(data):
    profile = ProfileReport(data, explorative=True)
    return profile

# If file is uploaded
if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.subheader('Data Overview')
    st.write(df)

    st.write('---')
    st.header('Data Profiling Report')
    profile_report = create_report(df)
    st_profile_report(profile_report)

else:
    st.info('Awaiting CSV file upload.')
    if st.button('Use Example Data'):
        df = sns.load_dataset('titanic')
        st.subheader('Data Overview')
        st.write(df)

        st.write('---')
        st.header('Data Profiling Report')
        profile_report = create_report(df)
        st_profile_report(profile_report)

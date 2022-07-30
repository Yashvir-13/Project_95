import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
st.set_page_config(page_title="Census visualisation app",page_icon=":money:",layout="centered",initial_sidebar_state="auto")
@st.cache()
def load_dataset():
    df=pd.read_csv("adult.csv")
    df.columns=['age','workclass','fnlwgt','education','education-years','marital-status','occupation','relationship','race','gender','capital-gain','capital-loss','hours-per-week','native-country','income']
    df['native-country'] = df['native-country'].replace(' ?',np.nan)
    df['workclass'] = df['workclass'].replace(' ?',np.nan)
    df['occupation'] = df['occupation'].replace(' ?',np.nan)
    df.dropna(inplace=True)
    df.drop(columns='fnlwgt',axis=1,inplace=True)
    return df
df=load_dataset()
st.title("Census visualisation app")
st.subheader("This app allows the user to explore and visualise census data.")
st.title("View data")
with st.beta_expander("View Dataset"):
	st.dataframe(df)
st.subheader("Columns's description")
if st.checkbox("Show summary"):
    st.write(df.describe())
col_1,col_2,col_3=st.beta_columns(3)
with col_1:
    if st.checkbox("Show column names"):
        st.write(df.columns)
with col_2:
    if st.checkbox("Show datatypes"):
        st.write(df.dtypes)
with col_3:
    if st.checkbox("Show column data"):
        col=st.selectbox("Select the column",tuple(df.columns))
        st.write(df[col])        	

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data (1990) by Yanan Wen')
df = pd.read_csv('housing.csv')


mid_filter = st.slider('Minimal Median House Value:', 0, 500001, 200000)  

st.subheader('See more filters in the sidebar:')

ocean_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  
     df.ocean_proximity.unique())  

df = df[df.median_house_value >= mid_filter]

income_filter = st.sidebar.radio(
    "choose income level",
    ('Low','Medium','High'))

df = df[df.ocean_proximity.isin(ocean_filter)]

if income_filter == 'Low' :
    df = df[df.median_income <= 2.5]
if income_filter == 'Medium':
    df = df[df.median_income < 4.5]
if income_filter == 'High':
    df = df[df.median_income > 4.5]


st.map(df)


st.subheader('Histogram of the Median House Value')
fig, ax= plt.subplots()
df.median_house_value.hist(ax=ax, bins = 30)
st.pyplot(fig)
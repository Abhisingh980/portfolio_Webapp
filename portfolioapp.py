import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("my img.jpg")


content = '''Hi,i am Abhinesh! i am a python programmer,developer, an founder of my self.I graduated in 2023
 with Master in computer application ,focus on using python for remote sensing.i have worked with companies from a
 various countries ,such as center for conservation Geography,to map and understand australian ecosystems  ,
 image processing with the swiss in terra ,and performing data mining to gain business insights with australian rapid 
  intelligence'''

content = content.title()
with col2:
    st.title(" Abhinesh kumar")
    st.info(content)

content = "Below You can find some of the apps I have built in pythin . feel free to contact me"

st.write(content)

df = pd.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])



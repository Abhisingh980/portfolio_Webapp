import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("my img.jpg")


content1 = '''Hi,i am Abhinesh! i am a python programmer,developer, an founder of my self.I graduated in 2023
 with Master in computer application ,focus on using python for remote sensing.i have worked with companies from a
 various countries ,such as center for conservation Geography,to map and understand australian ecosystems  ,
 image processing with the swiss in terra ,and performing data mining to gain business insights with australian rapid 
  intelligence'''

content1 = content1.title()
with col2:
    st.title(" Abhinesh kumar")
    st.info(content1)


col6, col7 = st.columns(2)
content2 = "Below You can find some of the apps I have built in pythin . feel free to contact me"
with col6:
    st.write(content2)


df = pd.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")



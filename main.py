import streamlit as st
import  pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("image/photo.jpg")

with col2:
    st.title("Abhishek Agrawal")
    content = """
    I am Abhishek Agrawal,I am a college student at SRM University, actively engaged in coading language Python.
    Passionate about programming and eager to explore its applications,
    I'm dedicated to honing my coding skills and fostering a promising future in the tech industry.
    """
    st.info(content)

content2 = """Below you can find some of the app I have built in Python. 
Feel free to contact me
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/" + row["image"])
        st.write(f"[Source code]({row['url']})")
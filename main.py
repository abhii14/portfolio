import streamlit as st

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




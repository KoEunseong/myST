import streamlit as st 
st.title("app title")
st.code(x = 2023)
st.sidebar.title("this is side bar")

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

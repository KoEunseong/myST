import streamlit as st 
import graphviz as graphviz
st.title("app title")
st.sidebar.title("this is side bar")

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)


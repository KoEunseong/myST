import streamlit as st 
import graphviz as graphviz

st.graphviz_chart('''
  digraph {
    Big_shark -> Tuna
    Tuna -> dong-won
    }
''')

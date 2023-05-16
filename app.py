import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np

rand=np.random.normal(1,2,size=20)
fig, ax = plt.subplots()
ax.hist(rand,bins=15)
st.pyplot(fig)

"""
st.title("app title")
st.sidebar.title("this is side bar")

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

st.graphviz_chart('''
  digraph {
    Big_shark -> Tuna
    Tuna -> dong-won
    }
''')
"""

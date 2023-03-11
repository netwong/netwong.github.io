import streamlit as st
from sklearn import datasets
import numpy as np
st.title("Streamlit example")

st.write("""
# Explore different classifier
which one is the best?
""")

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Brest Cancer", "Wine Dataset"))
classifer_name = st.sidebar.selectbox("Select Classifier", ("KNN", "SVM", "Random Forest"))


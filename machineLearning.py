import streamlit as st
from sklearn import datasets
import numpy as np
st.title("Streamlit example")

st.write("""
# Explore different classifier
which one is the best?
""")

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Brest Cancer", "Wine"))
classifer_name = st.sidebar.selectbox("Select Classifier", ("KNN", "SVM", "Random Forest"))

def get_dataset(dataset_name):
  if dataset_name == "Iris":
    data = dataset.load_iris()
  elsif dataset_name == "Breast Cancer":
    data = dataset.load_brest_cancer()
  else:
    data = dataset.load_wine()
    
  X = data.data
  y = data.target
  return X, y


X, y = get_dataset(dataset_name)
st.write("shape of dataset", X.shape)
st.write("number of classes", len(np.unique(y)))



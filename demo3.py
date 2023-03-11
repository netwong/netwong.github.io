import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np


x = np.linspace(0,10,100)
bar_x=[1,2,3,4,5]

opt = st.sidebar.radio("Select any graph", options=("Line", "Bar", "H-Bar"))
if opt == "Line":
  st.markdown("<h1 style='text-align:center;'>Line Chart</h1>")
  fig = plt.figure()
  # plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/blob/master/pacoty.mplstyle")
  plt.plot(x, np.sin(x))
  plt.plot(x, np.cos(x), '--')
  st.write(fig)
elif opt == "Bar":
  st.markdown("<h1 style='text-align:center;'>Line Chart</h1>")
  fig = plt.figure()
  plt.bar(x, x*10)
  st.write(fig)

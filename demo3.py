import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np


x = np.linspace(0,10,100)
opt = st.sidebar.radio("Select any graph", options=("Line", "Bar", "H-Bar"))
if opt == "Line"
  fig = plt.figure()
  plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/blob/master/pitayasmoothie-dark.mplstyle")
  plt.plot(x, np.sin(x))
  st.write(fig)
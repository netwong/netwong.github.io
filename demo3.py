import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np


x = np.linspace(0,10,100)
st.sidebar.write("Hello this is my side bar")

fig = plt.figure()
plt.plot(x, np.sin(x))
st.write(fig)

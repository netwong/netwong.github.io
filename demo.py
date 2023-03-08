import streamlit as st
from datetime import datetime

st.header("Demo page")
st.markdown("---")

st.title("Slider")
sliderValue = st.slider("This is a slider", min_value=1, max_value=5, step=1)
st.write(sliderValue)

currentTime = datetime.now()
start_time = st.slider( "When do you start?", value=currentTime, format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


st.markdown("---")
st.title("Uploading Files")
image = st.file_uploader("Please upload an image", type=["png", "jpg"])
if image is not None:
  st.image(image)
  

images = st.file_uploader("Please upload images", type=["png", "jpg"], accept_multiple_files=True)
if images is not None:
  for image in images:
    st.image(image)  
  
  
video = st.file_uploader("Please upload a video", type="mp4")
if video is not None:
  st.video(video)
  

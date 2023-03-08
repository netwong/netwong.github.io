import streamlit as st
from datetime import datetime

currentTime = datetime.now()

st.header("Demo page")
st.markdown("---")

st.title("Date Input")

dateInput = st.date_input("Enter the event date")
st.write(dateInput)



st.markdown("---")

st.title("Text Input")

textInput = st.text_input("Please input your favorite book name", max_chars=60)
st.write("The book you like most is ", textInput)




st.markdown("---")

st.title("Slider")
sliderValue = st.slider("This is a slider", min_value=1, max_value=5, step=1)
st.write(sliderValue)


start_time = st.slider( "When do you start?", value=datetime(2023, 3, 8, 10, 30), format="MM/DD/YY - hh:mm")
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
  

import streamlit as st


st.header("Demo page")
st.markdown("---")

st.title("Uploading Files")
image = st.file_uploader("Please upload an image", type=["png", "jpg"])
if image is not None:
  st.image(image)
  
video = st.file_uploader("Please upload a video", type="mp4")
if video is not None:
  st.video(video)
  

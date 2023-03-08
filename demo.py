import streamlit as st


st.header("Demo page")
st.markdown("---")

st.title("Uploading Files")
image = st.file_uploader("Please upload an image", type=["png", "jpg"])
if image is not None:
  st.image(image)
  

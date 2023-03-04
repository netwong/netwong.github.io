import streamlit as st
st.markdown("<h1 style='text-align: centre;'>URL Shortner</h1>", unsafe_allow_html=True)
form=st.form("name")
url=form.text_input("URL HERE")

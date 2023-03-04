import streamlit as st
import pyshorteners as pyst

shortners = pyst.Shortener()

st.markdown("<h1 style='text-align: centre;'>URL Shortner</h1>", unsafe_allow_html=True)
form=st.form("name")
url=form.text_input("URL HERE")
s_btn = form.form_submit_button("SHORT")
if s_btn:
  shorted_url = tinyurl.short(url)
  st.text(shorted_url)
  


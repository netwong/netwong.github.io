import streamlit as st
import pyshorteners as pyst

st.markdown("""
.css-1rs6os.edgvbvh3
{
  visibility: hidden;
}

.css-cio0dv.egzxvld1
{
  visibility: hidden;
}

.css-z3au9t.egzxvld2
{
  visibility: hidden;
}


""", unsafe_allow_html=True)


shortners = pyst.Shortener()

st.markdown("<h1 style='text-align: centre;'>URL Shortner</h1>", unsafe_allow_html=True)
form=st.form("name")
url=form.text_input("URL HERE")
s_btn = form.form_submit_button("SHORT")
if s_btn:
  shorted_url = shortners.tinyurl.short(url)
  st.text(shorted_url)
  


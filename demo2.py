import streamlit as st


st.markdown("<h1 style='text-align:center'>User Registration</h1>", unsafe_allow_html=True)
with st.form("Form 1"):
  col1, col2 = st.columns(2)
  col1.text_input("First Name")
  col2.text_input("Last Name")
  st.text_input("Email Address")
  col1.text_input("Password")
  col2.text_input("Confirm Password")
  st.form_submit_button('Submit')
  

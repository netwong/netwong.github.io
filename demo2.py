import streamlit as st


st.markdown("<h1 style='text-align:center'>User Registration</h1>", unsafe_allow_html=True)
with st.form("Form 1", clear_on_submit=True):
  col1, col2 = st.columns(2)
  fName = col1.text_input("First Name")
  lName = col2.text_input("Last Name")
  st.text_input("Email Address")
  st.text_input("Password")
  st.text_input("Confirm Password")
  day, month, year = st.columns(3)
  day.text_input("Day")
  month.text_input("Month")
  year.text_input("Year")
  fState = st.form_submit_button('Submit')
  if fState:
    if fName == "" and lName == "":
      st.warning("Please fill above fields")
    else:
      st.success("Submitted Sucessfully")
      

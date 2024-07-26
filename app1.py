import streamlit as st

st.title("Simple Form")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120)
submit = st.button("Submit")

if submit:
  st.write("Name:", name)
  st.write("Age:", age)

import streamlit as st


st.write("Hi")

option = st.selectbox(
  'What would you like to do?', 
  ('update', 'delete', 'insert'))

st.write('You selected:', option)

number = st.number_input("Enter number", 0, 25, 6, 2)
your_name = st.text_input("Enter your name")

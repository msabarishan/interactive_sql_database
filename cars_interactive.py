
import streamlit as st


st.write("Hi")

option = st.selectbox(
  'What would you like to do?', 
  ('update', 'delete', 'insert'))

if(option=='update'):
  st.write('Enter the employee id to be updated')
  
if(option=='delete'):
           st.write('Select the employee Id to be deleted' )
  
if(option=='insert'):
           st.write('Enter the new employee data')

number = st.number_input("Enter number", 0, 25, 6, 2)
your_name = st.text_input("Enter your name")

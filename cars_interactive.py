
import streamlit as st


st.write("Hi")

option = st.selectbox(
  'What would you like to do?', 
  ( ' ','update', 'delete', 'insert'))

if(option=='update'):
  st.write('Enter the employee id to be updated')
  number = st.number_input("Enter the employee number")
  
if(option=='delete'):
  st.write('Select the employee Id to be deleted' )
  number = st.number_input("Enter the employee number")
    
  
if(option=='insert'):
    st.write('Enter the new employee data')
    emp_id = st.number_input("Enter emp number",min_value=1, max_value=1000, step=1))
    first_name = st.text_input("Enter first name")
    last_name = st.text_input("Enter last name")
    birth_day = st.date_input("Enter date of birth")
    sex = st.selectbox('Select the gender', ('M', 'F'))
    salary = st.text_input("Enter salary")
    super_id = st.number_input("Enter sup_id")
    branch_id = st.number_input("Enter branch_id")
    


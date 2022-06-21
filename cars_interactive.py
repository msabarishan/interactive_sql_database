
import streamlit as st
import psycopg2
import postgreconnect
import pandas as pd


st.write("Hi")

option = st.selectbox(
  'Select one of the below option', 
  ('display','delete', 'insert'))

  
if(option=='delete'):
  st.write('Select the employee Id to be deleted' )
  company_data = """DELETE FROM employee  WHERE emp_id = 108 ;"""
  postgreconnect.runquery(company_data)
    
  
if(option=='insert'):
    st.write('Enter the new employee data')
    emp_id = st.number_input("Enter emp number",min_value=1, max_value=1000, step=1)
    first_name = st.text_input("Enter first name")
    last_name = st.text_input("Enter last name")
    birth_day = st.date_input("Enter date of birth")
    sex = st.selectbox('Select the gender', ('M', 'F'))
    salary = st.text_input("Enter salary")
    super_id = st.number_input("Enter sup_id")
    branch_id = st.number_input("Enter branch_id")
   
if(option=='display'):
  company_data='Select * from employee;'
  sql_data=pd.DataFrame(postgreconnect.runquery(company_data))
  sql_data.columns = ['emp_id','first_name','last_name','birth_day','Sex','salary','sup_id','branch_id']
  st.table(sql_data)
    
    


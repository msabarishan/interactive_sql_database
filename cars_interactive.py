import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import psycopg2
import postgreconnect
from altair import datum

st.write("Hi")
number = st.number_input("Enter number", 0, 25, 6, 2)
your_name = st.text_input("Enter your name")

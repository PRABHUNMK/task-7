import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import psycopg2
import postgreconnect

sql='select * from cars;'
record=pd.DataFrame(postgreconnect.runquery(sql))
print(record)
# record.columns=['Name','Miles_per_Gallon','Cylinders','Displacement','horsepower','Weight_In_Lbs','Acceleration','Years','Origin']
# st.title('Cars Data - Sourced from heroku')
# st.table(record)

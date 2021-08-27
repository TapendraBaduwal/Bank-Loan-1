import streamlit as st
from loan import loan_class #from loan.py file import loan_class
st.title("Loan Classification as per NRB Directive")
st.write("The bank loan can be classified according to the overdue of credit period time.")
#passing the overdue time in months.
overdue_time=int(st.text_input("Please enter your loan overdue time in months:"))
#function call
loan_type=loan_class(overdue_time)
#Using the "with" syntax
with st.form(key='my_form.'):
    loan_class=st.form_submit_button(label="Find Your loan type and make provision")
if loan_class:
    st.write(loan_type)
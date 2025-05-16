import streamlit as st

st.header("Consumer Loan Calculation Tool")

loan_amount = st.select_slider(
    "Amount",
    options=[1000, 2000, 3000, 4000, 5000]
)

loan_maturity = st.select_slider(
    "Month",
    options=[6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
)

st.subheader("Interest Rate")
st.text("%1")

calculation = ((loan_amount/100)*(1/365)*(loan_maturity*30)) + loan_amount

st.write("Your payback amount is: ", int(calculation))
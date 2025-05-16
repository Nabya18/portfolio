import streamlit as st

first_number = st.number_input("First Number")
second_number = st.number_input("Second Number")

buttons = st.columns(4)
with buttons[0]:
    button_addition = st.button("Addition (+)")
with buttons[1]:
    button_subtraction = st.button("Subtraction (-)")
with buttons[2]:
    button_multiplication = st.button("Multiplication (*)")
with buttons[3]:
    button_division = st.button("Division (/)")

if button_addition:
    st.write(f"Result : {first_number + second_number}")
if button_subtraction:
    st.write(f"Result : {first_number - second_number}")
if button_multiplication:
    st.write(f"Result : {first_number * second_number}")
if button_division:
    if second_number != 0:
        st.write(f"Result : {first_number / second_number}")
    else:
        st.write("Division by zero is not allowed.")
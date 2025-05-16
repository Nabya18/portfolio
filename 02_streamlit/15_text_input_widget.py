import streamlit as st

name = st.text_input("Enter your name")
surname = st.text_input("Enter your surname")

button = st.button("Show")

if button == True:
    st.write(f"Welcome {name} {surname} :raised_hand_with_fingers_splayed:")
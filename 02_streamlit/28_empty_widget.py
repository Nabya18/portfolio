import streamlit as st
import time

finish = "https://cdn-icons-png.flaticon.com/512/1505/1505465.png"

time_input = st.text_input("Enter a time")
button = st.button("Start")

if button:
    with st.empty():
        for seconds in range(int(time_input)):
            st.write(f"{seconds} seconds have passed")
            time.sleep(1)
        st.image(finish, width=100)
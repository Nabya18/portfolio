import streamlit as st

with st.form("my_form"):
    name = st.text_input("Name")
    surename = st.text_input("Surename")
    age = st.slider("How old are you?", 0, 100, 25)
    start_day = st.date_input("Start Day")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Name: {name}, Surename: {surename}, Age: {age}, Start Day: {start_day}")

st.write("Outsite of Form")
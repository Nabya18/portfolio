import streamlit as st

first_team = st.text_input("First team")
second_team = st.text_input("Second team")

t = st.time_input("Set an alarm for", value=None)

if st.button("Show"):
    st.write(f"The match between the {first_team} and {second_team} will start at {t}")
import streamlit as st
from database.queries import get_total_users

if not st.session_state.get("logged_in"):
    st.warning("Silakan login terlebih dahulu")
    st.switch_page("main.py")

total_users = get_total_users()

st.subheader("Total users")

col1 = st.columns(1)

with col1:
    st.metric(label="Total Users", value=total_users)
import streamlit as st
from database.queries import insert_user

st.title("Register")

with st.form("register_form"):
    name = st.text_input("name", label_visibility="collapsed", placeholder="👤 Name")
    email = st.text_input("email", label_visibility="collapsed", placeholder="📧 Email")
    password = st.text_input("password", type="password", label_visibility="collapsed", placeholder="🔒 Password")
    re_password = st.text_input("re-password", type="password", label_visibility="collapsed", placeholder="🔒 Re-Password")

    submitted = st.form_submit_button("Register")

    if submitted:
        if not name or not email or not password or not re_password:
            st.error("All fields are required.")
        elif password != re_password:
            st.error("Passwords do not match.")
        else:
            insert_user(name, email, password)
            st.success(f"Registration successful for {name}!")
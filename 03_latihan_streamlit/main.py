import streamlit as st
from database.queries import insert_user
from database.connection import check_login

if "page" not in st.session_state:
    st.session_state.page = "login"

def go_to(page_name):
    st.session_state.page = page_name

if st.session_state.page == "login":
    st.title("Login")

    with st.form("login_form"):
        email = st.text_input("email", label_visibility="collapsed", placeholder="📧 Email")
        password = st.text_input("password", type="password", label_visibility="collapsed", placeholder="🔒 Password")
        login_btn = st.form_submit_button("Login")

        if login_btn:
            if check_login(email, password):
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.success("Login successful!")
                st.switch_page("pages/Dashboard.py")
            else:
                st.error("Email atau password salah")

    if st.button("Belum punya akun? Register"):
        go_to("register")

elif st.session_state.page == "dashboard":
    if not st.session_state.get("logged_in"):
        st.warning("Please login to access the dashboard.")
        go_to("login")
        st.stop()

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_email = None
        go_to("login")

elif st.session_state.page == "register":
    st.title("Register")

    with st.form("register_form"):
        name = st.text_input("name", label_visibility="collapsed", placeholder="👤 Name")
        email = st.text_input("email", label_visibility="collapsed", placeholder="📧 Email")
        password = st.text_input("password", type="password", label_visibility="collapsed", placeholder="🔒 Password")
        re_password = st.text_input("re-password", type="password", label_visibility="collapsed", placeholder="🔒 Re-Password")

        register_btn = st.form_submit_button("Register")

        if register_btn:
            if not name or not email or not password or not re_password:
                st.error("All fields are required.")
            elif password != re_password:
                st.error("Passwords do not match.")
            else:
                try:
                    insert_user(name, email, password)
                    st.success(f"Registration successful for {name}!")
                    go_to("login")
                except Exception as e:
                    if "unique constraint" in str(e).lower():
                        st.error("Email already registered")
                    else:
                        st.error(f"Error: {e}")

    if st.button("Already have an account? Login"):
        go_to("login")
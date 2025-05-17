import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Javacripts")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuHnJDLOcdm_0b6N6kNj-1OvO9KhKYgqIy0w&s", width=100)
    st.link_button("Javascript Course","https://www.w3schools.com/js/DEFAULT.asp")

with col2:
    st.header("Python")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png", width=100)
    st.link_button("Python Course","https://www.w3schools.com/python/default.asp")

with col3:
    st.header("Java")
    st.image("https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg", width=100)
    st.link_button("Java Course","https://www.w3schools.com/java/default.asp")
import streamlit as st

Javascript = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuHnJDLOcdm_0b6N6kNj-1OvO9KhKYgqIy0w&s"
Python = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png"
Java = "https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg"

with st.expander("Javascript"):
    with st.container(border=True):
        st.image(Javascript, width=100)
        st.write("This is a Javascript container")

with st.expander("Python"):
    with st.container(border=True):
        st.image(Python, width=100)
        st.write("This is a Python container")

with st.expander("Java"):
    with st.container(border=True):
        st.image(Java, width=100)
        st.write("This is a Java container")
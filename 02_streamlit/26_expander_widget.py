import streamlit as st

Javascript = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuHnJDLOcdm_0b6N6kNj-1OvO9KhKYgqIy0w&s"
Python = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png"
Java = "https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg"

tab1, tab2, tab3 = st.tabs(["Python", "Javascript", "Java"])

with tab1:
    st.header("Python")
    st.image(Python, width=100)
    with st.expander("See explanation"):
        st.write("Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with the use of significant indentation.")

with tab2:
    st.header("Javascript")
    st.image(Javascript, width=100)
    with st.expander("See explanation"):
        st.write("JavaScript is a high-level, often just-in-time compiled, and multi-paradigm programming language. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions.")

with tab3:
    st.header("Java")
    st.image(Java, width=100)
    with st.expander("See explanation"):
        st.write("Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is a general-purpose programming language intended to let application developers write once, run anywhere (WORA).")
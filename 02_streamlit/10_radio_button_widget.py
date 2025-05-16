import streamlit as st

if "visibility" not in st.session_state:
    st.session_state.disabled = False

st.header("Choose Your Course")

radio_button = st.radio("Choose your course",
                        ["HTML | CSS :rainbow:",
                         "Python :snake:",
                         "JavaScript :computer:",
                         "Java :coffee:"],
                        index=None,
                        key="visibility",
                        disabled=st.session_state.disabled)

if radio_button == "HTML | CSS :rainbow:":
    st.write("You have selected HTML | CSS")
    st.session_state.disabled = True

if radio_button == "Python :snake:":
    st.write("You have selected Python")
    st.session_state.disabled = True

if radio_button == "JavaScript :computer:":
    st.write("You have selected JavaScript")
    st.session_state.disabled = True

if radio_button == "Java :coffee:":
    st.write("You have selected Java")
    st.session_state.disabled = True
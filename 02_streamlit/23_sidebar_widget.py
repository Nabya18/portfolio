import streamlit as st

st.header("**Welcome to the Streamlit Course!**")
st.video("https://youtu.be/rMLwiVrK3Fw")

with st.sidebar:
    add_selectbox = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home Phone", "Mobile Phone")
    )

    add_input = st.text_input("Info")

    add_radio = st.radio("Choose a shipping method",
                         ("Standard (5-15 days)", "Express (2-5 days)", "Overnight")
                         )

    send_button = st.button("Send")

if send_button:
    st.sidebar.write("Send button clicked")
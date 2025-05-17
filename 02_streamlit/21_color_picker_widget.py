import streamlit as st

color = st.color_picker("Pick A Color", "#000000")

st.markdown(f"<span style='color:{color}'>This is a text with the selected color</span>",
            unsafe_allow_html=True)

st.write("The selected color is", color)
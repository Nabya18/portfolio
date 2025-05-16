import streamlit as st

google = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"

size = st.slider("Select the size of the image", 100, 500, 200)
st.image(google, width=size, caption="Google " + str(size))
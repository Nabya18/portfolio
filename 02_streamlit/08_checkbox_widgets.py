import streamlit as st

st.header("Welcome to Nabya's Streamlit app")
black_cat = "https://new-s3.shelterluv.com/profile-pictures/5804077580cf235e064b5a0b7708c1bb/68e2f02fc41416adb06d2170ff63d454.jpeg"
tabby_cat = "https://new-s3.shelterluv.com/profile-pictures/f2b68d9a0b0a5495eecf9ef0e230e53b/82dee65564f9a214700bf2d184dc2534.jpeg"

image_list = [black_cat, tabby_cat]
caption_list = ["Black Cat", "Tabby Cat"]

checks = st.columns(2)
with checks[0]:
    images = st.checkbox("Do you want to see the images?")
with checks[1]:
    codes = st.checkbox("Do you want to see the code?")

if images:
    st.image(image=image_list, width=100, caption=caption_list)
if codes:
    st.code("Print('Hello World')")
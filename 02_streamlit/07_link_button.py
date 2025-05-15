import streamlit as st

black_cat = "https://new-s3.shelterluv.com/profile-pictures/5804077580cf235e064b5a0b7708c1bb/68e2f02fc41416adb06d2170ff63d454.jpeg"
tabby_cat = "https://new-s3.shelterluv.com/profile-pictures/f2b68d9a0b0a5495eecf9ef0e230e53b/82dee65564f9a214700bf2d184dc2534.jpeg"

image_list = [black_cat, tabby_cat]
caption_list = ["Black Cat", "Tabby Cat"]

st.header("Welcome to Nabya's Streamlit app")
st.image(image=image_list,
         width=100,
         caption=caption_list)
st.subheader('Cats are cute\
             love the cat')
st.link_button("Go to Nabya's Github",
               "https://github.com/Nabya18")
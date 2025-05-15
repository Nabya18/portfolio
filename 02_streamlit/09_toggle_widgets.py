import streamlit as st

st.header("Welcome to Nabya's Streamlit app")

toggles = st.columns(3)
with toggles[0]:
    toggle_image = st.toggle("Enable images")
with toggles[1]:
    toggle_audio = st.toggle("Enable audio")
with toggles[2]:
    toggle_video = st.toggle("Enable video")

if toggle_image:
    black_cat = "https://new-s3.shelterluv.com/profile-pictures/5804077580cf235e064b5a0b7708c1bb/68e2f02fc41416adb06d2170ff63d454.jpeg"
    tabby_cat = "https://new-s3.shelterluv.com/profile-pictures/f2b68d9a0b0a5495eecf9ef0e230e53b/82dee65564f9a214700bf2d184dc2534.jpeg"

    image_list = [black_cat, tabby_cat]
    caption_list = ["Black Cat", "Tabby Cat"]

    st.image(image=image_list,
             width=100,
             caption=caption_list)

if toggle_audio:
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
             start_time=100)

if toggle_video:
    st.video("https://www.youtube.com/watch?v=3JZ_D3ELwOQ",
             start_time=30)
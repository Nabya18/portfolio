import streamlit as st

# 04. Media elements
st.image("https://www.w3schools.com/w3images/lights.jpg",
         caption="This is a light",
         width=300)
st.video("https://www.youtube.com/watch?v=3JZ_D3ELwOQ",
         start_time=30)
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
         start_time=100)
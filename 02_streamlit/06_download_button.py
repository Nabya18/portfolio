import streamlit as st
import requests

# 06. Download button
image_url = "https://www.w3schools.com/w3images/lights.jpg"
st.image(image_url,
         caption="This is a light",
         width=300)

file_name = st.text_input("Enter file name with extension")
st.write(file_name)

# # buka file lokal
# with open("lights.jpg", "rb") as file:
#     btn = st.download_button(
#         label="Download file",
#         data=file,
#         file_name=file_name,
#         mime="text/plain"
#     )

# ambil file dari url
response = requests.get(image_url)
if response.status_code == 200:
    btn = st.download_button(
        label="Download file",
        data=response.content,
        file_name=file_name,
        mime="image/png"
    )
else:
    st.error("Gagal mengunduh gambar dari URL")
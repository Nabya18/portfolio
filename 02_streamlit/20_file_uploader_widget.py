import streamlit as st

uploaded_images = st.file_uploader("Choose a Image", accept_multiple_files=True)
uploaded_texts = st.file_uploader("Choose a Text", accept_multiple_files=True)

for uploaded_image in uploaded_images:
    st.write("filename:",uploaded_image.name)
    st.image(uploaded_image)

for uploaded_text in uploaded_texts:
    bytes_data = uploaded_text.read()
    st.write("filename:",uploaded_text.name)
    st.write(bytes_data.decode("utf-8"))
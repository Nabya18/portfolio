import streamlit as st

# 05. button Widgets
car_types = ["bmw", "mercedes", "toyota", "honda"]

car = st.text_input("Type your car name")

button = st.button("Check Availability")

if button == True:
    have_it = car.lower() in car_types
    if have_it:
        st.write(f"Yes, we have {car} in stock")
    else:
        st.write(f"Sorry, we don't have {car} in stock")
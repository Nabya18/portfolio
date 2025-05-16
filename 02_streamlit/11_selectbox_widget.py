import streamlit as st

st.header("Welcome to Nabya's Streamlit app")
st.subheader("Choose Your Car")

car_info = [{"CAR_MAKE": "Audi",
  "CAR_MODEL": "Q8",
  "CAR_YEAR": 2025,
  "CAR_PRICE": 70000},
 {"CAR_MAKE": "Mercedes",
  "CAR_MODEL": "GLA",
  "CAR_YEAR": 2023,
  "CAR_PRICE": 50000},
 {"CAR_MAKE": "BMW",
  "CAR_MODEL": "X5",
  "CAR_YEAR": 2023,
  "CAR_PRICE": 80000}]

option = st.selectbox("Which car did you like?",
                      [car_info[0]["CAR_MAKE"] + " " + car_info[0]["CAR_MODEL"],
                       car_info[1]["CAR_MAKE"] + " " + car_info[1]["CAR_MODEL"],
                       car_info[2]["CAR_MAKE"] + " " + car_info[2]["CAR_MODEL"]],)

Audi = "https://audiapproved.com/_next/image?url=https%3A%2F%2Fcdn.impel.io%2Fswipetospin-viewers%2Favme-samaco%2Fwa1zzzge4rb036241%2F20250102174422.TPZRWJ1A%2Fcloseups%2Fsrp_bg_vb_led.jpg&w=1920&q=75"
Mercedes = "https://www.clickmercedesbenz.com/file/MERCEDES-BENZ-GLA-400x250.jpg"
BMW = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQixtZ3mhuq_DjtgtTrHaR4LHrmcc0gQEkhIg&s"

if option == car_info[0]["CAR_MAKE"] + " " + car_info[0]["CAR_MODEL"]:
    st.image(Audi, width=300,
             caption="MODEL : " + str(car_info[0]["CAR_MODEL"]) + " " + \
                    "YEAR : " + str(car_info[0]["CAR_YEAR"]) + " " +
                    "PRICE : " + str(car_info[0]["CAR_PRICE"]))

if option == car_info[1]["CAR_MAKE"] + " " + car_info[1]["CAR_MODEL"]:
    st.image(Mercedes, width=300,
             caption="MODEL : " + str(car_info[1]["CAR_MODEL"]) + " " + \
                    "YEAR : " + str(car_info[1]["CAR_YEAR"]) + " " +
                    "PRICE : " + str(car_info[1]["CAR_PRICE"]))

if option == car_info[2]["CAR_MAKE"] + " " + car_info[2]["CAR_MODEL"]:
    st.image(BMW, width=300,
             caption="MODEL : " + str(car_info[2]["CAR_MODEL"]) + " " + \
                    "YEAR : " + str(car_info[2]["CAR_YEAR"]) + " " +
                    "PRICE : " + str(car_info[2]["CAR_PRICE"]))


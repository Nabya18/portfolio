import streamlit as st

tab1, tab2, tab3 = st.tabs(["Football", "Basketball", "Tennis"])

with tab1:
    st.header("Football")
    st.image("https://cdn.britannica.com/69/228369-050-0B18A1F6/Asian-Cup-Final-2019-Hasan-Al-Haydos-Qatar-Japan-Takumi-Minamino.jpg", width=100)
    st.write("Football is a team sport played between two teams of eleven players with a spherical ball. It is played by 250 million players in over 200 countries, making it the world's most popular sport.")

with tab2:
    st.header("Basketball")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9SIhIwS6OVHrGIRa_G_G_kMIg3xktu0I4WQ&s", width=100)
    st.write("Basketball is a team sport in which two teams, most commonly of five players each, opposing one another on a rectangular court, compete to shoot the basketball through the defender's hoop while preventing the opponent from shooting through their own hoop.")

with tab3:
    st.header("Tennis")
    st.image("https://cdn.britannica.com/57/183257-050-0BA11B4B/Roger-Federer-2012.jpg", width=100)
    st.write("Tennis is a racket sport that can be played individually against a single opponent (singles) or between two teams of two players each (doubles). Each player uses a racket that is strung with cord to strike a hollow rubber ball covered with felt over a net into the opponent's court.")
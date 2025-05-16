import streamlit as st
import datetime

name = st.text_input("Name")
company = st.text_input("Company name")

start_date = st.date_input("Start date", datetime.date(2023, 1, 1))
end_date = st.date_input("End date", datetime.date(2023, 1, 1))

pt1 = str(start_date).split("-")
pt2 = str(end_date).split("-")

t1 = datetime.date(year=int(pt1[0]), month=int(pt1[1]), day=int(pt1[2]))
t2 = datetime.date(year=int(pt2[0]), month=int(pt2[1]), day=int(pt2[2]))

if st.button("Show"):
    st.write(f"Welcome {name}! You worked at {company} for {(t2-t1).days} days :raised_hand_with_fingers_splayed:")
import streamlit as st

options = st.multiselect(
    "What are your favorite companies?",
    ["Google", "Apple", "Amazon", "Microsoft"],
    ["Google"]
)

google = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
apple = "https://www.apple.com/ac/structured-data/images/open_graph_logo.png?202301190335"
amazon = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7ZoPxHxiJ8nsrZTejjkVOIWcBlJt1D0KhLQ&s"
microsoft = "https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/RWCZER-Legal-IP-Trademarks-CP-MS-logo-740x417-1?wid=406&hei=230&fit=crop"

for x in options:
    if x == "Google":
        st.image(google, width=100, caption="Google")
    elif x == "Apple":
        st.image(apple, width=100, caption="Apple")
    elif x == "Amazon":
        st.image(amazon, width=100, caption="Amazon")
    elif x == "Microsoft":
        st.image(microsoft, width=100, caption="Microsoft")
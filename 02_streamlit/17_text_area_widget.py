import streamlit as st

list = []
txt = st.text_area(
    "Text to Analyze",
    "", placeholder="Type here...",
    max_chars=100
)

analyze_button = st.button("Analyze")

if analyze_button:
    text_split = txt.split(sep=" ")
    for word in text_split:
        list.append(word)
    st.write(f"You wrote {len(txt)} characters. You wrote {len(list)} words")
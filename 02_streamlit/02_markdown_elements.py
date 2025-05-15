import streamlit as st

# 02. markdown elements
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.markdown("### This is a markdown")

st.markdown("**This** is a markdown")
st.markdown("*This* is a markdown")

st.markdown("> this is a markdown")
st.markdown("1. This is first markdown\n2. This is second markdown\n3. This is third markdown")

str = "print('Hello World')"
st.code(str)
st.markdown("---")
st.markdown('[google](https://www.google.com)')

table = '''
| Name | Age |
|------|-----|
| Johny Andrean | 25  |
| Jane Ruby | 30  |
'''
st.markdown(table)

json = {"a": 1, "b": 2, "c": 3}
st.json(json)

st.markdown("This is an emoji :smile:")
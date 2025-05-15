import streamlit as st
import pandas as pd

# 03. Display elements
table = ({"Column 1": [1, 2, 3],
          "Column 2": [4, 5, 6],
         "Column 3": [7, 8, 9]})

st.table(table)
st.dataframe(table)
st.metric(label='Win speed',
          value='70ms',
          delta='5.7')
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "a": [70, 60, 40, 30, 80],
    "b": [50, 40, 60, 20, 90],
    "c": [30, 20, 50, 40, 70],
    "date": ["10/1", "10/2", "10/3", "10/4", "10/5"]
})

option = st.selectbox(
    "Stack Style",
    ["center", "normalize", "layered"]
)

st.area_chart(
    df,
    x="date",
    color=["blue","red","green"],
    stack=option,
)
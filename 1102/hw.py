import pandas as pd
import streamlit as st

st.write("學號: 112103011  姓名: 黃沛鈞")



df = pd.read_csv("https://raw.githubusercontent.com/ryanchung403/dataset/refs/heads/main/harry_potter.csv")

option = st.selectbox(
    "Stack Style",
    ["center", "normalize", "layered"]
)

st.area_chart(
    df,
    y=["revenue","budget"], 
    x="release_year",
    color=["blue","red"],
    stack=option,
)
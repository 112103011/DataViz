import streamlit as st
import pandas as pd

st.write("112103011 黃沛鈞")
st.write("哈利波特電影收益與預算")

df = pd.read_csv("https://raw.githubusercontent.com/ryanchung403/dataset/refs/heads/main/harry_potter.csv")


print(df)
colors = ["blue", "green"]

st.line_chart(df, y=["revenue","budget"], x="release_year", color=colors)
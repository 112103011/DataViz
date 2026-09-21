import streamlit as st
import pandas as pd
st.write("Titanic 資料")


df = pd.read_csv("https://raw.githubusercontent.com/ryanchung403/dataset/refs/heads/main/train_data_titanic.csv")

st.dataframe(df.style.highlight_max(axis=0))
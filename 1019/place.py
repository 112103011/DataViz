import pandas as pd
import streamlit as st

df = pd.DataFrame(
    data = [
        [24.965539418880798, 121.19119999322739, 1, "#FF00FF", "7-11學央門市"],
    ],
    columns=["lat", "lon", "size", "color", "scene"],
)

st.markdown(f"## :red[{df['scene'][0]}]", text_alignment="center")
st.markdown(f"### 學號：:blue[112103011] &nbsp;&nbsp;&nbsp; 姓名：:blue[黃沛鈞]")
st.markdown(f"### 位置：:blue[{df['lat'][0]}, {df['lon'][0]}]")
st.markdown(f"### 推薦理由：:blue[中央大學最好的餐廳]")

col1, col2 = st.columns(2)
with col1:
    st.map(df, 
       zoom=16,
       color="color",
       size="size",
)
with col2:
    st.image("https://lh3.googleusercontent.com/grass-cs/AABkmLe1iAj5tbqUeDFgaAETM6EIN0Y3oI7yjf-W1aAB8_euiQ8XCzOe7rVw0joYNInO5dZC6U_-sAb-9u7xLuFyn8CWnZvB2zRajx06ZiW_2IkMRIww-_w2i37Xk-qvQI7ytKCjRqtXeo2CMkpI=w408-h306-k-no", caption=df['scene'][0])
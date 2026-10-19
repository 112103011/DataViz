import pandas as pd
import streamlit as st

df = pd.DataFrame(
    data = [
        [25.0330, 121.5654, 10000, "#FF00FF", "Taipei"],
        [24.1852, 120.4695, 20000, "#00FF00", "Taichung"],
        [22.6514, 120.3737, 30000, "#0000FF", "Kaohsiung"]
    ],
    columns=["lat", "lon", "size", "color", "city"],
)

st.write("Taipei / Taichung / Kaohsiung")
st.map(df, 
       zoom=6.3,
       color="color",
       size="size",
)
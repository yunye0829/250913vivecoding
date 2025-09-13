import streamlit as st
import plotly.io as pio

st.title("MBTI 유형별 비율이 가장 높은 국가 TOP10")

# Load the Plotly figure
fig = pio.read_json("top10_mbti_countries.json")

# Display the figure
st.plotly_chart(fig)


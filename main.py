import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("MBTI 유형별 비율이 가장 높은 국가 TOP10")

# 파일 경로 설정
file_path = "countriesMBTI_16types.csv"

# 파일 존재 여부 확인 후 로드
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.success("기본 CSV 파일을 성공적으로 불러왔습니다.")
else:
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("업로드된 CSV 파일을 성공적으로 불러왔습니다.")
    else:
        st.warning("CSV 파일이 필요합니다.")
        st.stop()

# 컬럼 정리
df.columns = df.columns.str.strip()
mbti_types = df.columns[1:]  # 'Country' 제외

# MBTI 유형별 상위 10개 국가 추출
top10_data = []
for mbti in mbti_types:
    top10 = df[['Country', mbti]].sort_values(by=mbti, ascending=False).head(10)
    top10['MBTI'] = mbti
    top10_data.append(top10)

top10_df = pd.concat(top10_data)

# Plotly 그래프 생성
fig = px.bar(top10_df, x='Country', y=top10_df.columns[1], color='MBTI',
             facet_col='MBTI', facet_col_wrap=4,
             title='MBTI 유형별 비율이 가장 높은 국가 TOP10',
             labels={top10_df.columns[1]: '비율'})

# 그래프 출력
st.plotly_chart(fig)

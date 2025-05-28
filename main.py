pip install plotly
import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
DATA_URL = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    return df

df = load_data()

# 데이터 구조 확인
st.write("### 데이터 미리보기", df.head())

# 사용자 선택
numeric_cols = df.select_dtypes(include='number').columns.tolist()
categorical_cols = df.select_dtypes(include='object').columns.tolist()

x_axis = st.selectbox("X축 컬럼 선택", numeric_cols)
y_axis = st.selectbox("Y축 컬럼 선택", numeric_cols)
color_by = st.selectbox("색상 기준 (카테고리)", [None] + categorical_cols)

# Plotly 그래프
fig = px.scatter(
    df,
    x=x_axis,
    y=y_axis,
    color=color_by,
    title=f"{x_axis} vs {y_axis}",
    hover_data=df.columns
)

st.plotly_chart(fig)

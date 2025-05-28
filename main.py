import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
DATA_URL = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

df = load_data()

# 데이터 미리보기
st.write("### 데이터 미리보기", df.head())

# 컬럼 선택
all_columns = df.columns.tolist()

x_axis = st.selectbox("X축 컬럼 선택", all_columns)
y_axis = st.selectbox("Y축 (숫자값)", df.select_dtypes(include='number').columns.tolist())

# 막대그래프 그리기
fig = px.bar(df, x=x_axis, y=y_axis, title=f"{x_axis}별 {y_axis} 막대그래프")

st.plotly_chart(fig)

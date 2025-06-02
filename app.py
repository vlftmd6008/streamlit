import streamlit as st

st.title("안녕하세요 👋")
st.write("이것은 Streamlit + GitHub 연동 예제입니다.")

name = st.text_input("이름을 입력하세요:")
if name:
    st.success(f"{name}님, 반가워요!")

st.write("2일 중앙선거관리위원회에 따르면 21대 대선 유권자 수는 4439만1871명이다. 역대 최대 규모다. 인구는 줄고 있지만 고령화 추세로 성인 유권자가 늘었다.")
st.write("김예원")


import streamlit as st

st.title("안녕하세요 👋")
st.write("이것은 Streamlit + GitHub 연동 예제입니다.")

name = st.text_input("이름을 입력하세요:")
if name:
    st.success(f"{name}님, 반가워요!")


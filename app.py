import streamlit as st

from datetime import datetime
from pytz import timezone

now = datetime.now(timezone('Asia/Seoul'))


st.title(f"안녕하세요👋 이 글은 {now}에 마지막으로 편집되었습니다!")
st.write(" ## 이것은 여론조사 결과로 2025년 22대 대통령 선거를 예측해보는 글입니다.")



name = st.text_input("이름을 입력하세요:")
if name:
    st.success(f"{name}님, 반가워요!")

st.write("6월 2일 중앙선거관리위원회에 따르면 21대 대선 유권자 수는 4439만1871명입니니다. \
         이것은 역대 최대 규모입니다. 인구는 줄고 있지만 고령화 추세로 성인 유권자가 늘었습니다.")

st.write("여론조사결과는 중앙선거관리위원회의 중앙선거여론조사심의위원회 홈페이지에서 발췌했습니다.\
         대부분의 여론조사는 무선전화면접 또는 무선ARS로 진행했으며 표본추출 방식은 성, 연령, 지역 할당 후 \
         무선 가상번호를 추출했습니다. 사후층화를 했지만 성별, 연령별, 지역별로 가중값을 부여했으니 \
         Simple Random Sampling(단순임의추출출)을 Without replacement(비복원추출)한 것으로 추정량을 사용하겠습니다.")

st.write("# 김서연 고생했어요.")










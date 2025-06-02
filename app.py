import streamlit as st
import os
from datetime import datetime, timedelta, timezone

# 🕒 KST 시간대 설정 (UTC+9)
KST = timezone(timedelta(hours=9))

# 📄 경로 설정
try:
    APP_FILE = __file__
except NameError:
    # __file__이 동작하지 않을 경우 (ex. Jupyter)
    APP_FILE = r"C:\Users\cohok\OneDrive\문서\GitHub\streamlit\app.py"

LOG_FILE = "updated.txt"

# ✅ 마지막 수정 시간 가져오기
def get_last_modified_time(path):
    return os.path.getmtime(path)

# ✅ KST 기준 datetime 변환
def format_timestamp_kst(ts):
    return datetime.fromtimestamp(ts, tz=timezone.utc).astimezone(KST).strftime("%Y-%m-%d %H:%M:%S")

# ✅ 이전 기록된 시간 읽기
def read_previous_logged_time():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return float(f.readline().strip())
    return None

# ✅ 기록 갱신
def write_update_time(ts):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(str(ts))

# 🔍 현재 수정 시각
current_modified_time = get_last_modified_time(APP_FILE)

# 🔁 이전 시각과 비교
previous_time = read_previous_logged_time()

# ⏱️ 변경되었으면 기록
if previous_time != current_modified_time:
    write_update_time(current_modified_time)
    updated_time_str = format_timestamp_kst(current_modified_time)
    status = "✅ 코드가 변경되어 자동으로 기록되었습니다."
else:
    updated_time_str = format_timestamp_kst(previous_time or current_modified_time)
    status = "ℹ️ 최근에 코드 변경이 없습니다."

st.title(f"안녕하세요👋 이 글은 {updated_time_str}에 마지막으로 편집되었습니다!")
st.write("## 이것은 여론조사 결과로 2025년 22대 대통령 선거를 예측해보는 글입니다.")



name = st.text_input("이름을 입력하세요:")
if name:
    st.success(f"{name}님, 반가워요!")

st.write("6월 2일 중앙선거관리위원회에 따르면 21대 대선 유권자 수는 **4439만1871명**입니니다. \
         이것은 역대 최대 규모입니다. 인구는 줄고 있지만 고령화 추세로 성인 유권자가 늘었습니다.")

st.write("여론조사결과는 중앙선거관리위원회의 중앙선거여론조사심의위원회 홈페이지에서 발췌했습니다.\
         대부분의 여론조사는 무선전화면접 또는 무선ARS로 진행했으며 표본추출 방식은 성, 연령, 지역 할당 후 \
         무선 가상번호를 추출했습니다. 사후층화를 했지만 성별, 연령별, 지역별로 가중값을 부여했으니 \
         Simple Random Sampling(단순임의추출출)을 Without replacement(비복원추출)한 것으로 추정량을 사용하겠습니다.")



st.write("## 🧐우리에게 필요한 표본 수는 얼마일까?")
st.write(f"유한한 모집단이고 크기가 매우 크므로 우리가 필요한 표본 크기 n은 n= {n}로 계산할 수 있습니다. \
         여기서 z는 신뢰수준에 해당하는 z값 (예: 95% → z≈1.96)이고,")
st.write("p는 특성의 비율 (예: 성공 확률, 보통 보수적으로 0.5 사용), q는 1−p, 즉 실패 확률,")
st.write("B는 허용오차 (margin of error) (예: 0.05 = ±5%) 를 나타냅니다.")
















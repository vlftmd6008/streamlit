import streamlit as st
import os
from datetime import datetime, timedelta, timezone


KST = timezone(timedelta(hours=9))

# 절대 경로가 확실하면 직접 지정 (파일 위치 확인 후 수정)
# APP_FILE = r"C:\Users\cohok\OneDrive\문서\GitHub\streamlit\app.py"

# 아니면 현재 작업 디렉토리 기준 상대경로로 시도
APP_FILE = os.path.abspath("app.py")

LOG_FILE = os.path.abspath("updated.txt")

def get_last_modified_time(path):
    try:
        return os.path.getmtime(path)
    except Exception as e:
        st.error(f"❌ 파일 수정 시간 확인 실패: {e}")
        return None

def format_timestamp_kst(ts):
    return datetime.fromtimestamp(ts, tz=timezone.utc).astimezone(KST).strftime("%Y-%m-%d %H:%M:%S")

def read_previous_logged_time():
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                return float(f.readline().strip())
        except:
            return None
    return None

def write_update_time(ts):
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write(str(ts))
    except Exception as e:
        st.error(f"❌ 로그 저장 실패: {e}")

ts = get_last_modified_time(APP_FILE)

if ts is not None:
    prev_ts = read_previous_logged_time()
    if ts != prev_ts:
        write_update_time(ts)
        status = "✅ 코드가 변경되어 기록되었습니다."
    else:
        status = "ℹ️ 최근 코드 변경이 없습니다."
    
    time_str = format_timestamp_kst(ts)
    st.title(f"안녕하세요👋 이 글은 {time_str} 에 마지막으로 편집되었습니다!")
    st.info(status)
else:
    st.error("🚫 app.py 파일을 찾을 수 없습니다. 경로를 확인해주세요.")


st.write("## 이것은 여론조사 결과로 2025년 21대 대통령 선거를 예측해보는 글입니다.")

name = st.text_input("이름을 입력하세요:")
if name:
    st.success(f"{name}님, 반가워요!")

st.write("6월 2일 중앙선거관리위원회에 따르면 21대 대선 유권자 수는 **4439만1871명**입니니다. \
         이것은 역대 최대 규모입니다. 인구는 줄고 있지만 고령화 추세로 성인 유권자가 늘었습니다.")

st.write("여론조사결과는 중앙선거관리위원회의 중앙선거여론조사심의위원회 홈페이지에서 발췌했습니다.\
         대부분의 여론조사는 무선전화면접 또는 무선ARS로 진행했으며 표본추출 방식은 성, 연령, 지역 할당 후 \
         무선 가상번호를 추출했습니다. 사후층화를 했지만 성별, 연령별, 지역별로 가중값을 부여했으니 \
         Simple Random Sampling(단순임의추출)을 Without replacement(비복원추출)한 추정량을 사용하겠습니다.")



st.write("## 🧐우리에게 필요한 표본 수는 얼마일까?")
st.write("유한한 모집단이므로 우리가 필요한 표본 크기 n은")
st.latex(r"""
n = \frac{N z^2 p q}{(N - 1) B^2 + z^2 p q}
""")
st.write("로 계산할 수 있습니다.")
st.write("여기서 z는 신뢰수준에 해당하는 z값 (예: 95% → z≈1.96)이고,")
st.write("p는 특성의 비율 (예: 성공 확률, 보통 보수적으로 0.5 사용), q는 1−p, 즉 실패 확률,")
st.write("B는 허용오차 (margin of error) (예: 0.05 = ±5%) 를 나타냅니다.")

st.title("#### 📊 표본 크기 계산기")

st.markdown("#### 공식을 사용해 표본 수 n을 자동 계산해볼 수 있습니다:")
st.latex(r"""
n = \frac{N z^2 p q}{(N - 1) B^2 + z^2 p q}
""")

# 👉 사용자 입력
N = st.number_input("모집단 크기 N", min_value=1, value=1000)
z = st.number_input("✅ z 값 (예: 1.96)", value=1.96)
p = st.number_input("✅ p 값 (예: 0.5)", min_value=0.0, max_value=1.0, value=0.5)
B = st.number_input("✅ B 값 (허용 오차, 예: 0.05)", min_value=0.0001, value=0.05)

# 자동 계산
q = 1 - p
numerator = N * z**2 * p * q
denominator = (N - 1) * B**2 + z**2 * p * q

n = numerator / denominator

st.success(f"📊 필요한 표본 수 n ≈ {n:.2f}")

st.write("모집단인 전체 유권자는 4439만1871명이고 대부분의 여론조사는 95% 신뢰수준에 ±3.1%를 허용 오차로 두므로")
st.write("N = 44,391,871")
st.write("z = 1.96")
st.write("p = 0.5       (여기서 p는 특정 정당 지지율이나 특정 후보 지지율. 보수적으로 p=0.5로 설정)")
st.write("B = 0.031")
st.write("을 대입하면")

st.write("필요한 표본 수 n ≈ 99,998명") 
st.write("즉, **10만명 이상**의 사람들이 여론조사에 응답해야 95% 신뢰수준에 ±3.1%를 \
         허용 오차로, 표본이 전체 유권자를 대표한다고 할 수 있습니다.")

st.write("하지만 현실적으로 전화를 통해 이루어지는 여론조사는 응답률이 낮기 때문에 표본 수가 만 명을 넘기기 힘듭니다.")
st.write("작은 표본을 사용하면 어떤 특성(예: 연령, 성별, 지역 등)에 따라 응답 경향이 다를 수 있습니다. \
         또한, 여론조사나 표본조사에서 응답자의 인구 비율이 모집단의 인구 비율과 다르므로 결과의 대표성을 높이기 위해 \
         여른조사기관들은 사후 층화를 하여 가중치를 조정합니다.")
st.write("그러므로 우리는 비교적 적은 표본 수에도 층화 추출을 이용하여 표본의 대표성과 신뢰성을 얻을 수 있습니다.")

st.write("그럼 각 여론조사결과에 허용 오차를 적용해보면")

!pip install pdfplumber


import pdfplumber
import re

# 95% 신뢰수준 → z = 1.96
Z = 1.96

def extract_candidate_support(text, candidate_name):
    """텍스트에서 특정 후보 지지율(%) 추출"""
    pattern = rf"{candidate_name}[^\d]*(\d{{1,2}}(?:\.\d+)?)\s*%"
    match = re.search(pattern, text)
    return float(match.group(1)) if match else None

def calculate_margin(p, n=1000, z=Z):
    """표본 비율 p에 대한 오차범위 계산"""
    p /= 100  # 백분율 → 비율
    B = z * ((p * (1 - p)) / n) ** 0.5
    return round(B * 100, 2)  # 다시 백분율로

# Streamlit UI
st.title("🗳️ 여론조사 지지율 추출기")
uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type="pdf")

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text()

    candidates = ["이재명", "김문수", "이준석"]
    st.header("📊 지지율 및 오차범위 (±)")

    for name in candidates:
        support = extract_candidate_support(full_text, name)
        if support:
            margin = calculate_margin(support)
            st.metric(label=f"{name}", value=f"{support:.1f}%", delta=f"±{margin:.1f}%")
        else:
            st.warning(f"'{name}' 후보의 지지율 정보를 찾을 수 없습니다.")
            

import streamlit as st

from datetime import datetime
from pytz import timezone

now = datetime.now(timezone('Asia/Seoul'))


st.title(f"안녕하세요👋 이 글은 {now}에 마지막으로 편집되었습니다!")
st.write("고생했어요요")
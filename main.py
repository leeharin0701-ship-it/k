import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="✨ MBTI별 여행지 추천",
    page_icon="✈️",
    layout="centered"
)

# 메인 타이틀 및 소개
st.title("💖 나의 MBTI 찰떡궁합 여행지 찾기 💖")
st.markdown("---")
st.write("안녕! 👋 당신의 **MBTI**를 선택하면, 두근두근 설레는 맞춤형 국내외 여행지를 추천해 줄게요! 🌍✨")

# MBTI 입력 받기 (셀렉트박스 활용)
col1, col2 = st.columns(2)

with col1:
    mbti_1 = st.selectbox("성향 1", ["E (외향형)", "I (내향형)"])
    mbti_3 = st.selectbox("성향 3", ["T (사고형)", "F (감정형)"])

with col2:
    mbti_2 = st.selectbox("성향 2", ["S (감직형)", "N (직관형)"])
    mbti_4 = st.selectbox("성향 4", ["J (계획형)", "P (인식형)"])

# 선택한 MBTI 조합 만들기
user_mbti = mbti_1[0] + mbti_2[0] + mbti_3[0] + mbti_4[0]

# 추천 데이터 딕셔너리
travel_recommendations = {
    "ENFP": {
        "place": "스페인 바르셀로나 🇪🇸",
        "reason": "자유로움과 예술이 넘치는 도시! 새로운 사람들과 어울리기 좋아하는 당신에게 딱이에요.",
        "tip": "가나다라 골목길을 자유롭게 산책해보세요!"
    },
    "INTJ": {
        "place": "아이슬란드 레이캬비크 🇮🇸",
        "reason": "조용하고 신비로운 자연 속에서 깊은 사색을 즐길 수 있는 완벽한 여행지!",
        "tip": "오로라 투어는 미리 철저하게 계획하는 센스!"
    },
    "ISFP": {
        "place": "강릉 안목해변 🌊",
        "reason": "파도 소리를 들으며 예쁜 카페에서 여유를 만끽할 수 있는 힐링 스팟.",
        "tip": "따뜻한 커피 한 잔 들고 백사장 걷기 추천!"
    },
    "ESTJ": {
        "place": "싱가포르 🇸🇬",
        "reason": "치안이 좋고 완벽하게 정돈된 시스템! 효율적인 일정을 좋아하는 당신에게 최고.",
        "tip": "마리나 베이 샌즈 야경 코스를 꼼꼼히 짜보세요."
    },
}

# 기본 추천 데이터 (딕셔너리에 없는 MBTI를 위한 기본값)
default_recommendation = {
    "place": "제주도 서귀포 🍊",
    "reason": "누구에게나 사랑받는 아름다운 섬! 맛있는 음식과 예쁜 풍경이 가득해요.",
    "tip": "바다가 보이는 감성 카페는 필수 코스!"
}

# 결과 확인 버튼
st.markdown("---")
if st.button("✈️ 내 여행지 확인하기!", use_container_width=True):
    st.balloons() # 축하 풍선 효과!
    
    # 결과 가져오기
    result = travel_recommendations.get(user_mbti, default_recommendation)
    
    st.success(f"당신의 MBTI **{user_mbti}**를 위한 맞춤 추천입니다! 🎉")
    
    # 결과 카드 출력
    st.markdown(f"### 🌟 추천 여행지: **{result['place']}**")
    st.info(f"**추천 이유:** {result['reason']}")
    st.warning(f"💡 **여행 꿀팁:** {result['tip']}")

# 하단 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with 💖 for your lovely trip!</p>", unsafe_allow_html=True)

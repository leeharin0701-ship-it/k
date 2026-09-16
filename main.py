import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="✨ MBTI 랜덤 여행지 추천",
    page_icon="🎒",
    layout="centered",
)

# 메인 타이틀 및 소개
st.title("💖 MBTI 랜덤 찰떡궁합 여행지 뽑기 💖")
st.markdown("---")
st.write(
    "안녕! 👋 당신의 **MBTI**를 선택하면, 매번 두근두근 설레는 국내외 여행지를 랜덤으로 하나씩 추천해 줄게요! 🌍✨"
)

# MBTI 입력 받기 (셀렉트박스 활용)
col1, col2 = st.columns(2)

with col1:
  mbti_1 = st.selectbox("성향 1", ["E (외향형)", "I (내향형)"])
  mbti_3 = st.selectbox("성향 3", ["T (사고형)", "F (감정형)"])

with col2:
  mbti_2 = st.selectbox("성향 2", ["S (감각형)", "N (직관형)"])
  mbti_4 = st.selectbox("성향 4", ["J (계획형)", "P (인식형)"])

# 선택한 MBTI 조합 만들기
user_mbti = mbti_1[0] + mbti_2[0] + mbti_3[0] + mbti_4[0]

# MBTI 성향별 다양한 여행지 리스트 (각 MBTI별로 여러 곳 수록)
travel_database = {
    "ENFP": [
        {
            "place": "스페인 바르셀로나 🇪🇸",
            "reason": (
                "자유로움과 예술이 넘치는 도시! 새로운 사람들과 어울리기 좋아하는"
                " 당신에게 딱이에요."
            ),
            "tip": "가나다라 골목길을 자유롭게 산책해보세요!",
        },
        {
            "place": "태국 방콕 🇹🇭",
            "reason": (
                "화려한 야시장과 에너지가 넘치는 곳! 매 순간 새로운 즐거움이"
                " 기다리고 있어요."
            ),
            "tip": "카오산 로드에서 전 세계 친구들과 맥주 한잔?",
        },
        {
            "place": "부산 광안리 🌊",
            "reason": (
                "바다와 화려한 야경, 그리고 맛있는 음식이 가득한 활기찬 해양 도시!"
            ),
            "tip": "밤에 드론쇼를 보면서 감성 충전하기!",
        },
    ],
    "INTJ": [
        {
            "place": "아이슬란드 레이캬비크 🇮🇸",
            "reason": (
                "조용하고 신비로운 자연 속에서 깊은 사색을 즐길 수 있는 완벽한"
                " 여행지!"
            ),
            "tip": "오로라 투어는 미리 철저하게 계획하는 센스!",
        },
        {
            "place": "일본 교토 🇯🇵",
            "reason": (
                "역사와 전통이 살아 숨 쉬는 고즈넉한 사찰과 고요한 골목길이 있는"
                " 곳."
            ),
            "tip": "사람이 적은 이른 아침 시간에 산책 코스를 짜보세요.",
        },
        {
            "place": "강원도 정선 🌲",
            "reason": "깊은 산속 오롯이 나 혼자만의 시간에 집중할 수 있는 힐링 스팟.",
            "tip": "조용한 독채 펜션에서 밀린 책 읽기 추천!",
        },
    ],
    "ISFP": [
        {
            "place": "강릉 안목해변 ☕",
            "reason": (
                "파도 소리를 들으며 예쁜 카페에서 여유를 만끽할 수 있는 힐링"
                " 스팟."
            ),
            "tip": "따뜻한 커피 한 잔 들고 백사장 걷기 추천!",
        },
        {
            "place": "발리 우붓 🇮🇩",
            "reason": (
                "초록빛 푸른 논밭과 예술가들의 영감이 가득한 마음의 안식처."
            ),
            "tip": "요가 클래스를 들으며 몸과 마음을 정화해 보세요.",
        },
        {
            "place": "제주도 구좌읍 🍊",
            "reason": (
                "조용한 돌담길과 아기자기한 소품샵들이 기다리고 있는 감성 풍만"
                " 동네."
            ),
            "tip": "바다가 보이는 독립 서점에서 여유 부리기.",
        },
    ],
    "ESTJ": [
        {
            "place": "싱가포르 🇸🇬",
            "reason": (
                "치안이 좋고 완벽하게 정돈된 시스템! 효율적인 일정을 좋아하는"
                " 당신에게 최고."
            ),
            "tip": "마리나 베이 샌즈 야경 코스를 꼼꼼히 짜보세요.",
        },
        {
            "place": "미국 뉴욕 🗽",
            "reason": (
                "세계의 중심! 한 치의 오차도 없이 바쁘게 돌아가는 도시의 매력을"
                " 느껴보세요."
            ),
            "tip": "타임스퀘어와 브로드웨이 뮤지컬 예약은 필수!",
        },
        {
            "place": "서울 강남/도심 호캉스 🏙️",
            "reason": (
                "모든 인프라가 완벽하게 갖추어진 편리한 도시 속 럭셔리 휴가."
            ),
            "tip": "분단위로 짜인 완벽한 맛집 투어 계획 세우기.",
        },
    ],
}

# 기본 추천 데이터 (딕셔너리에 직접 등록되지 않은 MBTI를 위한 기본 풀)
default_recommendations = [
    {
        "place": "제주도 서귀포 🍊",
        "reason": "누구에게나 사랑받는 아름다운 섬! 맛있는 음식과 예쁜 풍경이 가득해요.",
        "tip": "바다가 보이는 감성 카페는 필수 코스!",
    },
    {
        "place": "스위스 인터라켄 🇨🇭",
        "reason": "눈부신 알프스 대자연 속에서 맑은 공기를 마시며 리프레시하기 좋은 곳.",
        "tip": "융프라우요흐 올라갈 때는 초콜릿 챙기기!",
    },
    {
        "place": "포르투갈 리스본 🇵🇹",
        "reason": "노란 트램과 낭만적인 노을이 반겨주는 유럽의 숨은 보석 같은 도시.",
        "tip": "에그타르트 원조 맛집에서 1인 3개 이상 먹기!",
    },
]

# 세션 스테이트를 이용해 새로고침/버튼 클릭 시 랜덤 결과 유지 관리
if "random_choice" not in st.session_state:
  st.session_state.random_choice = None

st.markdown("---")

# 버튼 배치 (메인 뽑기 버튼)
if st.button("🎲 랜덤 여행지 뽑기!", use_container_width=True):
  st.balloons()  # 축하 풍선 효과!

  # 해당 MBTI의 리스트를 가져오고, 없으면 기본 리스트 사용
  pool = travel_database.get(user_mbti, default_recommendations)
  # 랜덤으로 하나 쏙 뽑기!
  st.session_state.random_choice = random.choice(pool)

# 결과가 있으면 화면에 출력
if st.session_state.random_choice:
  result = st.session_state.random_choice

  st.success(
      f"당신의 MBTI **{user_mbti}**를 위해 룰렛을 돌려 뽑은 행운의 여행지입니다! 🎉"
  )

  # 결과 카드 출력
  st.markdown(f"### 🌟 추천 여행지: **{result['place']}**")
  st.info(f"**추천 이유:** {result['reason']}")
  st.warning(f"💡 **여행 꿀팁:** {result['tip']}")

  # 다시 뽑기 버튼
  if st.button("🔄 마음에 안 들어? 다른 곳 다시 뽑기!", use_container_width=True):
    pool = travel_database.get(user_mbti, default_recommendations)
    st.session_state.random_choice = random.choice(pool)
    st.rerun()

# 하단 푸터
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with 💖 for your"
    " lovely trip!</p>",
    unsafe_allow_html=True,
)

파이썬 언어로 작성한 디스코드 봇입니다.(동아리 과제용도로 작성)
채워야할 부분은 다음과 같습니다.

TOKEN = 'your bot token'
API_ENDPOINT = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
SCHOOL_CODE = '0000000000000'  # 실제 학교 코드 입력
API_KEY = '0000000000000000000000'  # 실제 API 키 입력

사용하는 모듈은 다음과 같습니다.
discord.py==1.7.3(인텐트 관련)
requests
datetime
re 

API_KEY는 나이스 개방포털에서 신청 가능합니다.
학교 코드는 데이터 셋에서 아무 데이터나 클릭후 자신의 학교를 검색하면 됩니다.(행정표준코드)

2차 수정 가능합니다.

명령어
따로 접두사 없습니다. 추가하실분은 알아서 추가하세용
예시) 급식표 20231130
      #2023년 11월 30일 점심 급식표 출력
예시) 시간표 1 1
      #1학년 1반 시간표 출력


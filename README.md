파이썬 언어로 작성한 디스코드 봇입니다.(동아리 과제용도로 작성)
채워야할 부분은 다음과 같습니다.
-
TOKEN = 'your bot token'
API_ENDPOINT = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
SCHOOL_CODE = '0000000000000'  # 실제 학교 코드 입력
API_KEY = '0000000000000000000000'  # 실제 API 키 입력
-
사용하는 모듈은 다음과 같습니다.
discord.py==1.7.3(인텐트 관련)
requests
datetime
re 

API_KEY는 나이스 개방포털에서 신청 가능합니다.
학교 코드는 데이터 셋에서 아무 데이터나 클릭후 자신의 학교를 검색하면 됩니다.(행정표준코드)

2차 수정 가능합니다.

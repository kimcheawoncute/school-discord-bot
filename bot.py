import discord
import requests
from datetime import datetime
import re  # re 모듈 추가

TOKEN = 'your bot token'
API_ENDPOINT = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
SCHOOL_CODE = '0000000000000'  # 실제 학교 코드 입력
API_KEY = '0000000000000000000000'  # 실제 API 키 입력

client = discord.Client()

# 급식 정보를 가져오는 함수
def get_meal_info(school_code, date):
    params = {
        'KEY': API_KEY,
        'Type': 'json',
        'ATPT_OFCDC_SC_CODE': 'N10',
        'SD_SCHUL_CODE': school_code,
        'MLSV_FROM_YMD': date,
        'MLSV_TO_YMD': date
    }

    response = requests.get(API_ENDPOINT, params=params)
    meal_data = response.json()

    try:
        meal_info = meal_data['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
        # <br/>을 \n으로 대체
        meal_info = meal_info.replace('<br/>', '\n')
        return meal_info
    except IndexError:
        return "입력한 날짜의 급식 정보를 가져올 수 없습니다."

# 봇이 준비되었을 때 실행되는 이벤트 핸들러
@client.event
async def on_ready():
    print(f'{client.user}로 로그인했습니다!')
    print('------')

# 메시지가 수신되었을 때 실행되는 이벤트 핸들러
@client.event
async def on_message(message):
    # 봇이 보낸 메시지는 무시
    if message.author == client.user:
        return

    # '도움말' 명령어에 대한 응답
    if message.content == '도움말':
        await message.channel.send('급식표 조회: "급식표 <날짜>" (예시: 급식표 20231201)')

    # '급식표' 명령어에 대한 응답
    if message.content.startswith('급식표'):
        # 입력한 메시지를 공백으로 분리하여 명령어와 날짜를 분리
        command, *args = message.content.split()
        
        if len(args) == 1 and len(args[0]) == 8 and args[0].isdigit():
            meal_date = args[0]
            meal_info = get_meal_info(SCHOOL_CODE, meal_date)
            await message.channel.send(f'날짜: {meal_date}\n급식표:\n{meal_info}')
        else:
            await message.channel.send('올바른 날짜를 입력해주세요. (예시: 급식표 20231201)')

    # '시간표' 명령어에 대한 응답
    if message.content.startswith('시간표'):
        command, grade, class_num = message.content.split()
        timetable_info = get_timetable(SCHOOL_CODE, grade, class_num)
        timetable_info = re.sub(r"요일: \d{8}, ", "", timetable_info)  # 요일 삭제
        today_date = datetime.now().strftime("%Y-%m-%d")
        
        embed = discord.Embed(
            title=f'{grade}학년, {class_num}반의 시간표',
            description=f'{timetable_info}',
            color=discord.Color.green()
        )
        embed.set_footer(text=f'{today_date}의 시간표 입니다')
        await message.channel.send(embed=embed)

client.run(TOKEN)

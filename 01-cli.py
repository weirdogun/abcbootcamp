from dotenv import load_dotenv 
load_dotenv() 
# 앞선 ai.py 내 함수를 활용합니다. 
from ai import get_personality_analysis 
print("안녕하세요! AI 관상가입니다.") 
print("당신의 얼굴 특징을 알려주시면 성격과 미래를 분석해드릴게요.") 
# 유저로부터 1줄 문자열을 입력받아 변수에 저장합니다. 
face_description = input("얼굴 특징을 입력하세요 (예시: 둥근 얼굴, 큰 눈, 높은 코, 두꺼운 입술 등) : ") 
# 함수를 호출하여 관상을 봅니다. 
result = get_personality_analysis(face_description) 
# 관상 분석 결과를 출력합니다. 
print("---") 
print(" 관상 분석 결과") 
print(result) 
print("분석이 완료되었습니다. 감사합니다! #")
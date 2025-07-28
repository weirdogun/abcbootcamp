# 라이브러리 설치 필요 : pip install --upgrade openai
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=API_KEY)  # OPENAI_API_KEY 환경변수 지정이 필요

response = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn in korean.",
)

print("usage :", response.usage)
print(response.output_text)



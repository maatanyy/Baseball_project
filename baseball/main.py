from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 값을 가져오기
my_key = os.getenv('MY_KEY')

# 값을 출력
print(f"MY_KEY: {my_key}")
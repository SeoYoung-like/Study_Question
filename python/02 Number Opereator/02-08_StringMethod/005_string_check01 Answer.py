filename1 = "black.jpg"
filename2 = "white.png"

# 1. 마지막 문자열이 'png'로 끝나는지 확인하기
print(f"{filename1.endswith('png')} {filename2.endswith('png')}")

# 2. 문자열의 구성 파악하기
# 소문자만 구성 되어 있는지 확인 / 대문자로만 구성되어 있는지 확인
print(f"{filename1.islower()} {filename2.isupper()}")
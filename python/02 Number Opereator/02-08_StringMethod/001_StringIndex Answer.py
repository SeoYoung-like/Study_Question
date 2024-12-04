a = "Life is too short. 'Python' is the best choice."

# 1. 문자의 개수 세기 'o'
print(a.count("o"))

# 2. 처음 등장 위치 알아내기 "is"       - 없을시 -1반환
print(a.find("is"))

# 3. 마지막 등장 위치 알아내기 "is"     - 없을시 -1반환
print(a.rfind("is"))

# 4. 인덱스 반환하기 (왼쪽) "is"        - 없을시 에러 발생
print(a.index("is"))

# 5. 인덱스 반환하기 (오른쪽) "is"      - 없을시 에러 발생
print(a.rindex("is"))

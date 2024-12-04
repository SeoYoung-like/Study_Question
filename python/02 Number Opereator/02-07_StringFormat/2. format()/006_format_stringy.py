
str = "String"
num = 1024


# [문자길이]  첫 번째 칸: 8칸  /  두 번째 칸: 5칸
print("{} | {}".format(str, num))

# 왼쪽 정렬 / 문자 길이: 10
print("{}".format(str))

# 오른쪽 정렬 / 문자 길이: 10
print("{}".format(str))

# 가운데 정렬 / 문자 길이: 10
print("{}".format(str))

# 특정 문자로 공백 채우기 ( 문자 길이: 10 )
print("{}".format(str))       # 왼쪽 정렬   / 공백 - '!' 문자로 채우기
print("{}".format(str))       # 가운데 정렬 / 공백 - '=' 문자로 채우기
print("{}".format(num))      # 오른쪽 정렬 / 공백 - '@' 문자로 채우기 / 부호 붙이기


float_number = 15875.14159273


# 소수점 아래 자리가 4개가 되도록 절삭
print("{:0.4f}".format(float_number))             # 1번째 : 일반적인 방법
print("{:.4f}".format(float_number))              # 2번째 : 0생략

# 공백 추가 - 총 10글자가 되도록 빈칸 추가, 소수점 아래 자리가 4개가 되도록 절삭
print("{:10.4f}".format(float_number))

# 부호, 0숫자 추가 - 총 10글자가 되도록 빈칸 추가, 소수점 아래 자리가 4개가 되도록 절삭
print("{:+010.4f}".format(float_number))

# 의미 없는 소수 제거하기
print("{:g}".format(52.000))
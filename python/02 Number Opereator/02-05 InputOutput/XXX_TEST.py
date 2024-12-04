# 공백으로 분리된 숫자를 연속해서 입력 받은 후 각각 n과 m에 저장한다.
# 1. n과 m을 각각 출력한다.
# 2. n x m 값을 출력한다.
# 빈 줄을 채우시오.


# ( 기본형 )
print("[ 입력1 ]")
arr = str.split(input())
n = int(arr[0])
m = int(arr[1])

print(n)
print(m)
print(n * m)
print()


# ( 단축형 )
print("[ 입력2 ]")
n, m = str.split(input())

print(n)
print(m)
print(int(n) * int(m))
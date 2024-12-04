# 공백으로 분리된 숫자를 연속해서 입력 받은 후 각각 n과 m에 저장한다.
# 1. n과 m을 각각 출력한다.
# 2. n x m 값을 출력한다.

# ( 기본형 )
print("[ 입력1 ]")
arr = input("첫 번째 입력 : ").split()
n = int(arr[0])
m = int(arr[1])

print(n)
print(m)
print(n * m)
print()


# ( 단축형 )
print("[ 입력2 ]")
n, m = input("두 번째 입력 : ").split()

print(n)
print(m)
print(int(n) * int(m))

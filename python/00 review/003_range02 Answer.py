# 10부터 0까지 역순으로 된 리스트를 만들고 출력하시오.
# 10 9 8 7 ... 3 2 1 0
# [방법1] 순수 range
# [방법2] 함수 사용

A = list(range(10, 0 - 1, -1))
B = list(reversed(range(0, 11)))

for i in A:
    print(i, end=" ")

print()

for i in B:
    print(i, end=" ")

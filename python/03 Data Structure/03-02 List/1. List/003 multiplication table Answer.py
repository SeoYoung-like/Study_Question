# 구구단 결과가 들어있는 리스트를 완성하시오. ( 컴프리헨션 사용 )

# 두 줄 사용
arr = [i * j for i in range(2, 10)
           for j in range(1, 10)]

index = 0
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {arr[index]}")
        index = index + 1
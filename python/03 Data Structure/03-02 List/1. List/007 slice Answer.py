# [ 입력 값 ]
# [Dave],[David],[Andy],[Arthor]

# [ 결과 값 ]
# Dave
# David
# Andy
# Arthor


data = input()

for str in data.split(","):
    print(str[1:-1])
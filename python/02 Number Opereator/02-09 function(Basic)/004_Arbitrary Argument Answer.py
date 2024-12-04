# 1. 가변 매개변수를 사용하여 코드를 완성하시오. 
# 2. 각 원소의 값을 하나씩 출력하시오.

def print_many(*args):
    for arg in args:
        print(arg)


li = [1, 2, 3, 4, 5]
print_many(*li)



# 1. "key : value" 이 형태로 출력되는 함수를 작성하시오. - items() 사용
def print_many(**kwargs):
    for key, val in kwargs.items():
        print(key, ' : ', val, sep='')


# 2. 조건문과 key를 활용하여 빈 칸을 채우시오.
def personal_info(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])


dic = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}

print("==================")
print_many(**dic)
print("==================")
personal_info(**dic)
print("==================")


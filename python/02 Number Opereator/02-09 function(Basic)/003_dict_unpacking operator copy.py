data = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}

# 이름, 나이, 주소 순으로 출력하는 함수를 작성하시오. (주의!) **kwargs를 사용하지 마시오.
def personal_info(name, age, address):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)

# dictionary를 언패킹하여 함수를 사용하시오.
personal_info(*data)
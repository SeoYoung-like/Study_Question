
example_list = ["요소A", "요소B", "요소C"]

# enumerate 객체 출력합니다.
print("# enumberate() 함수 적용 출력")
print(enumerate(example_list))
print()

# enumerate 객체를 list() 함수로 강제 변환해서 출력합니다.
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

# for 반복문과 enumerate() 함수 조합해서 사용하기1 - index와 value를 출력합니다.
print("# 반복문과 조합하기1")
for index, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(index, value))
print()

# for 반복문과 enumerate() 함수 조합해서 사용하기2 - index 시작점 1로 변경
print("# 반복문과 조합하기2")
for index, value in enumerate(example_list, start=1):
    print("{}번째 요소는 {}입니다.".format(index, value))
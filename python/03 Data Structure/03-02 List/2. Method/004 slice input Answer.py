# 슬라이싱를 활용하여 대입(수정) 인덱스 1부터 2사이에 값에 ["A", "B", "C"] 원소를 추가하시오.

my_list = [0, 1, 2, 3, 4, 5]
print(id(my_list))

my_list[1:3] = ["A", "B", "C"]
print(id(my_list))

print(my_list)
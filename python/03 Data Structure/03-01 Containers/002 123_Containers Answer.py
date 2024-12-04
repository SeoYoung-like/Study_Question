# [문제] 1,2,3과 관련된 데이터 각 컨테이너 형 별로 선언하기

# 1. 컨테이너 함수 사용 ( O )
print("-------[ 자료 선언1 ]-------")
list_val = list([1,2,3])
tuple_val = tuple((1,2,3))
dict_val = dict({1:1, 2:2, 3:3})
set_val = set([1,2,3])
print(f"{'list:':12} {str(list_val):20} {str(type(list_val)):10}")
print(f"{'tuple:':12} {str(tuple_val):20} {str(type(tuple_val)):10}")
print(f"{'dictionary:':12} {str(dict_val):20} {str(type(dict_val)):10}")
print(f"{'set:':12} {str(set_val):20} {str(type(set_val)):10}")
print("---------------------------")

print()

# 2. 컨테이너 함수 사용 ( X )
print("-------[ 자료 선언2 ]-------")
list_val = [1,2,3]
tuple_val = (1,2,3)
dict_val = {1:1, 2:2, 3:3}
set_val = set([1,2,3]) #{} 사용불가
print(f"{'list:':12} {str(list_val):20} {str(type(list_val)):10}")
print(f"{'tuple:':12} {str(tuple_val):20} {str(type(tuple_val)):10}")
print(f"{'dictionary:':12} {str(dict_val):20} {str(type(dict_val)):10}")
print(f"{'set:':12} {str(set_val):20} {str(type(set_val)):10}")
print("---------------------------")

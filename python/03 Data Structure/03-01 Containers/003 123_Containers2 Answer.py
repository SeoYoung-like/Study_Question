# [문제] 1,2,3과 관련된 데이터 각 컨테이너 형 별로 선언하기

# range() 함수 사용 ( O )
print("-------[ 자료 선언3 ]-------")
list_val = list(range(1,4))
tuple_val = tuple(range(1,4))
dict_val = dict()
set_val = set(range(1,4))
print(f"{'list:':12} {str(list_val):20} {str(type(list_val)):10}")
print(f"{'tuple:':12} {str(tuple_val):20} {str(type(tuple_val)):10}")
print(f"{'dictionary:':12} {str(dict_val):20} {str(type(dict_val)):10}")
print(f"{'set:':12} {str(set_val):20} {str(type(set_val)):10}")
print("---------------------------")

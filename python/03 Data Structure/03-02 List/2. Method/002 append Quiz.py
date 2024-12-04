# 다음의 결과값을 유추하고 설명하시오.
my_list = [1, 2, 3]
print("append 전 :", id(my_list))

my_list.append("추가1")
print("append 수정1 :", id(my_list)) 
print(my_list)

my_list = my_list.append(5)
print("append 수정2 :", id(my_list)) 
print(my_list)

print()


new_list = my_list.append("추가2")
print(id(new_list))
print(type(new_list))
print(new_list)








# [ 1번 문제 ]
# append 메써드를 사용해도 id는 변하지 않는다.
# 단, 대입 연산자를 이상하게 사용할 경우 id는 변할 수 있다.

# [ 2번 문제 ]
# append 메써드는 return이 없다.
# 즉, 새로운 객체가 만들어 지더라도 NoneType이로 저장되는 것이다.
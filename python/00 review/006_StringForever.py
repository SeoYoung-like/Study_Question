int_a = [10, 20, 30, 15, 20, 40]
int_b = int_a[0:1000]
str_a = "ABCDEF"
str_b = str_a[0:1000]

print("=" * 20)

print("int a :", int_a)
print("int b :", int_b)
print("string a :", str_a)
print("string b :", str_b)

print("=" * 20)

print("id(int a) :", id(int_a))
print("id(int b) :", id(int_b))
print("id(string a) :", id(str_a))
print("id(string b) :", id(str_b))

print("=" * 20)

print("(int) a == b :", int_a == int_b)
print("(int) a is b :", int_a is int_b)
print("(string) a == b :", str_a == str_b)
print("(string) a is b :", str_a is str_b)

print("=" * 20)
# 다음 코드의 결과를 설명하시오.



















# [추측1] 컨테이너 선언시 컨테이너 내부의 값이 같더라도 서로 다른 객체를 만든 것이다. ( 나의 추측 )
# c = a이가 리스트를 다른 변수에 할당하고, 2 개가 된 것 같지만 실제로는 리스트가 1 개 입니다.
# c, a는 꼬릿말일 뿐이다.
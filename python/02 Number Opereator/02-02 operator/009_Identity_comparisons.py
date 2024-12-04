a = [10, 20, 30, 15, 20, 40]
b = [10, 20, 30, 15, 20, 40]
c = a
d = a[0:1000]


print("=" * 20)

print("a :", a)
print("b :", b)
print("c :", c)
print("d :", d)

print("=" * 20)

print("id(a) :", id(a))
print("id(b) :", id(b))
print("id(c) :", id(c))
print("id(d) :", id(d))

print("=" * 20)

print("a == b :", a == b)
print("a == c :", a == c)
print("a == d :", a == d)

print("=" * 20)

print("a is b :", a is b)
print("a is c :", a is c)
print("a is d :", a is d)

print("=" * 20)
# 다음 코드의 결과를 설명하시오.



















# [추측1] 컨테이너 선언시 컨테이너 내부의 값이 같더라도 서로 다른 객체를 만든 것이다. ( 나의 추측 )
# c = a이가 리스트를 다른 변수에 할당하고, 2 개가 된 것 같지만 실제로는 리스트가 1 개 입니다.
# c, a는 꼬릿말일 뿐이다.
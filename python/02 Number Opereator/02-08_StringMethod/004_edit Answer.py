# 1. 문자열을 새로운 문자열로 바꾸시오. (Hello => King)
s = "Hello World! Welcome to Korea"

print(s.replace("World", "King"))


# 2. 구분자 문자열과 이터러블의 요소를 연결하여 새로운 문자열로 만드세요.
c = '|'
s = ['a', 'b', 'c', 'd']

print(c.join(s))


# 3. 변환 테이블을 사용해서 문자열을 바꾸시오. ( 추측 : 암호화 )
s = "apple"

table = str.maketrans("aeiou", "12345")
print(s.translate(table))

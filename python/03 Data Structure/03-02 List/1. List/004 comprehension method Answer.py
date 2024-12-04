# fruits 리스트 중 문자열만 뽑아서 공백을 제거 한 후 모두 대문자로 만드시오.

fruits = ['  banana', '  loganberry ', 77, 'passion fruit', 54]

new_fruits = [fruit.strip().upper() for fruit in fruits if not(str(fruit).isalnum())]
print(new_fruits)
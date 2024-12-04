# ValueError 주의! : 자료형을 변환할 때 '변환할 수 없는 것'을 변환 하려고 하면 ValueError 예외가 발생한다.
# 15.2 넣을 시 발생한다.

string_number = input("입력A> ")

int_a = int(string_number)			#int cast
print(type(int_a))

float_a = float(string_number)		#float cast
print(type(float_a))

string_a = str(int_a)				#string cast
print(type(string_a))
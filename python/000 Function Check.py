temp_data = [1,2,3,4,5]
before_data = [1,2,3,4,5]
id_before = id(temp_data)


fuc = "strip"
code_str = f"temp.{fuc}()"
del temp_data[3]
id_after = id(temp_data)


print("=" * 50)
print(f"[ {fuc} ]")
print(f"VALUABLE DATA : {temp_data}")
print(f"CODE : {code_str}")

print()

print("비파괴적/파괴적 메서드 : ", end="")
if temp_data == before_data :
    print("비파괴적 메서드")
else:
    print("파괴적 메서드")

print("리턴값 : ", end="")
if return_value == None :
    print("NO")
else:
    print("YES")

print("원본 데이터 - 주소 유지(유무) : ", end="")
if id_before == id_after :
    print(f"YES")
else :
    print(f"NO")
print("=" * 50)

print(f"~ 메서드 사용 전 ~")
print("메서드 사용 전 (id) :", id_before)
print(f"변수 데이터 : {before_data}")
print(f"리턴 값 : None")
print("=" * 50)
 
print(f"~ 메서드 사용 후 ~")
print("메서드 사용 후 (id) :", id_after) 
print(f"변수 데이터 : {temp_data}")
print(f"리턴 값 : {return_value}")
print("=" * 50)
# 1. 양쪽 공백을 지우시오.
# 2. 왼쪽 공백을 지우시오.
# 3. 오른쪽 공백을 지우시오.
a = "  Hi  "

print(a.strip())
print(a.lstrip())
print(a.rstrip())


# 4. 특정 구두점 ',.'을 지우시오.
# 5. and 동시에 양쪽 공백까지 지우시오.
s = ",  python ...."

print(s.strip(".,"))
print(s.strip(",.").strip())

import random
import time


start = time.time()
my_list01 = [random.randrange(10000, 50000) * random.randrange(1, 50) for _ in range(1000000)]
end = time.time()
print(f"1차 : {end - start}초")

start = time.time()
my_list02 = list(random.randrange(10000, 50000) * random.randrange(1, 50) for _ in range(1000000))
end = time.time()
print(f"2차 : {end - start}초")

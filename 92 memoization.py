from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*5


print(fx(10))
print(fx(20))
print(fx(10))
print(fx(30))
print(fx(40))
print(fx(20))
print(fx(10))
print(fx(20))
print(fx(10))
print(fx(30))
print(fx(40))
print(fx(20))
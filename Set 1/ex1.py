from math import gcd
from functools import reduce

def cmmdc(*numere):
    return reduce(gcd, numere)

print(cmmdc(12, 18, 24))   # 6
print(cmmdc(8, 12))        # 4
print(cmmdc(100, 75, 50, 25))  # 25
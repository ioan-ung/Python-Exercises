import re
from functools import reduce

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def largest_prime_from_string(text):
    numbers = re.findall(r"\d+", text)
    numbers = [int(x) for x in numbers if is_prime(int(x))]
    max_prime = reduce(lambda x,y:max(x,y),numbers)

    return max_prime

text = "Am 3 mere si 25 de pere.71"
print(largest_prime_from_string(text))

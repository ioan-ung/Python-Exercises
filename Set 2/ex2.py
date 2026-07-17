def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
def get_primes(numbers):
    primes = []

    for number in numbers:
        if is_prime(number):
            primes.append(number)
    return primes

numbers = [2, 4, 5, 8, 11, 15, 17]
print(get_primes(numbers))
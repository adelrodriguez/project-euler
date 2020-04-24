from math import sqrt
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

num = 600851475143
limit = int(sqrt(num))


def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


result = max(n for n in range(int(sqrt(num))) if is_prime(n) and num % n == 0)

print(f'The result is {result}')

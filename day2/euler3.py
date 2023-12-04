import math


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def largest_prime_factor(n: int) -> int:
    result = n
    while result > 0:
        if is_prime(result) and n % result == 0:
            return result
        else:
            result -= 1


def prime_factors(n: int) -> list[int]:
    i = 2
    result = []
    while n > 1:
        while n % i == 0:
            result.append(i)
            n //= i
        i += 1
    return result




assert(is_prime(2))
assert(is_prime(3))
assert(not is_prime(4))
assert(not is_prime(9))
assert(not is_prime(21))
assert(is_prime(17))

assert(largest_prime_factor(13195) == 29)
print(max(prime_factors(600851475143)))

print(max(prime_factors(13195)))
max_found = 0
for i in range(100, 1_000):
    for j in range(100, 1_000):
        product = i * j
        if str(product) == str(product)[::-1] and product > max_found:
            max_found = product

print(max_found)

import itertools

three_digit_numbers = range(10, 1_000)
pairs = itertools.product(three_digit_numbers, repeat=2)
products = (i * j for (i, j) in pairs)
palindroms = (p for p in products if str(p) == str(p)[::-1])
print(max(palindroms))


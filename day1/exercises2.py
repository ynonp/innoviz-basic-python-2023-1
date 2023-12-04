# Exercises 2
# Course Example Project
# https://github.com/ynonp/innoviz-basic-python-2023-1

# From Project Euler:
# 1. https://projecteuler.net/problem=1
# Answer: 233168

# 2. https://projecteuler.net/problem=4
# Answer: 906609
# Hints: Convert numbers to strings
# Hints: Use "123"[::-1] to reverse a string

# 3. https://projecteuler.net/problem=6
# Answer: 25164150
sum_of_numbers = 0
for i in range(1_000):
    if (i % 3 == 0) or (i % 5 == 0):
        print(f"{i} is a multiplication of 3 or 5")
        sum_of_numbers += i

print(sum_of_numbers)


for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        candidate = i * j
        # if it's a palindrom
        if str(candidate) == str(candidate)[::-1]:
            print(candidate)
            break














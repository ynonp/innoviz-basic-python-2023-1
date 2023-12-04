x = [10, 20, 30]
y = ['a', 'b', 'c']
z = [10, 20, 'a', 'b', [5, 4], [2], True]
a = []

## List Operations
# 7. length
len(x)

# 6. Item Access by index
print(x[1])

# 4. Search
print(10 in x)
print(x.index(20))

# 8. Reverse
print(x[::-1])
list(reversed(x))

# 5. Sort
print(sorted(x))
t = ['one', 'two', 'three', 'four', 'five']
assert(sorted(t) == ['five', 'four', 'one', 'three', 'two'])
assert(sorted(t, key=len) == ['one', 'two', 'four', 'five', 'three'])

# 2. Append
x.append(40)
x.append(50)

# 3. Remove
# delete by value
x.remove(30)
# delete last
x.pop()
# delete by index
del(x[0])

# 1. Iteration
for item in x:
    print(item)

for index, item in enumerate(x):
    print(f"{index}. {item}")


# 9. Take a sublist
# x[start:end:step]
# WARNING - y = x is not the same as y = x[::]


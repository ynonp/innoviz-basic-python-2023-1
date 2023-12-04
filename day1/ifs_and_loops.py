# Ifs and Loops
#

# 1. Conditions
favorite_number = int(input("what's your lucky number?"))
if 100 > favorite_number > 10 and 2 < 5:
    print("wow it's a big number")
    print("wow it's a big number")
    print("wow it's a big number")
# can have more than 1 elif, or none at all
elif favorite_number > 5:
    print("wow it's a medium number")
# else is optional, but you can only have one
else:
    print("wow it's a small number (or very big)")


# Loop
number = 99
while number > 10:
    number = int(input())


while True:
    number = int(input())
    if number > 10:
        break

# prints the numbers from 0 to 9
for i in range(10):
    print(i)



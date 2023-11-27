# replit.com - write and run code in any language

# Lesson 1 - Basic Commands

# print() is a function that prints text to screen
# we create strings with "..." or '...'
print("Hello Python")
print("print is a python function that puts text on the screen")
print('Example usage: print("hello world")')
print("Example usage: print('hello world')")

##
# 1. Read things from user
# 2. Define variables
# 3. If
# 4. Do things multiple times
#

## 1. Read things from user
# input() - read some text from a user

## 2. Define some variables

name = "ynon"
email = "ynon@ynonperek.com"

print(name)
print("name")

# print and evaluate {...} blocks
print(f"My name is {name}")

# 1 + 1 is valid python code -> returns 2
print(f"1 + 1 = {1 + 1}")

# two is a variable holding the *number* 2
two = 1 + 1

# what_is_this is a variable holding the string "1bccb1"
what_is_this = "1bc" + "cb1"

# this will raise a TypeError Exception so it's commented out
# what_is_that = "1" + 1

# Print the text "who are you?"
# Then stop the program, wait for the user to type a line
# (reading until EOL / Enter)
# And THEN assign the text as the value of "name"
name = input("who are you? ")
print(f"welcome, {name}")

favorite_number = int(input("Pick a number... "))
print(f"{favorite_number} + 1 = {favorite_number + 1}")

########################################
# Exercises - With break Until 11:30
#
# 1. Read someone's age in years, print out the age in months
#    (user types: 2, you say back 24)
#
# 2. Read someone's age in months, print out the age in years
#
# 3. Read sum of money in NIS, print out the sum in USD
#












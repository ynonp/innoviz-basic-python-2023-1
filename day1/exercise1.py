from py_currency_converter import convert

########################################
# Exercises - With break Until 11:30
#
# Using f-strings
# https://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf
#
# List of python operators
# https://docs.python.org/3/library/operator.html
#
# Pypi - python module directory
# https://pypi.org
#
# 1. Read someone's age in years, print out the age in months
#    (user types: 2, you say back 24)
#
# 2. Read someone's age in months, print out the age in years
#
# 3. Read sum of money in NIS, print out the sum in USD
#

age_in_years = int(input("how old are you? (in years)"))
print(f"wow then you must be {age_in_years * 12} months old")

age_in_months = int(input("how old are you? (in months)"))
print(f"wow then you must be {age_in_months / 12} years old")
print(f"wow then you must be {age_in_months / 12 : .4f} years old")

# x // y => integer division, for example 10 // 3 == 3
age_in_years = age_in_months // 12

# 10 % 3 =>
remainder = age_in_months % 12
print(f"wow then you must be {age_in_years} years and {remainder} months old")

nis = int(input("amount in NIS: "))
usd = nis * 0.27
print(f"You have {usd}$")
print(convert(base='ILS', amount=nis, to=['USD', 'EUR']))

story = """
one time I went to the doctor
and she told me I should get some
new medications but then I didn't want
it so I went to another doctor
"""

print(story)










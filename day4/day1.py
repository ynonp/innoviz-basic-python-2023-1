import io

demo_text = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
# with open('...') as f:

for line in io.StringIO(demo_text):
    print(line, end='')

# Take first and last digit from each line,
# sum the values
# result should be: 142

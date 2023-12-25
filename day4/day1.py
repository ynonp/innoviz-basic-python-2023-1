import io
import re

def line_to_calibration_value(line: str) -> int:
    first_digit_match = re.search(r'\d', line)
    first_digit = first_digit_match.group(0)
    #print(f"First digits in line: {line.strip()} is {first_digit}")

    last_digit_match = re.search(r'\d', line[::-1])
    last_digit = last_digit_match.group(0)
    #print(f"Last digit is: {last_digit}")

    calibration_value = int(f"{first_digit}{last_digit}")
    return calibration_value

demo_text = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
# with open('...') as f:

calibration_value = sum([line_to_calibration_value(line) for line in io.StringIO(demo_text)])
print(calibration_value)


# Take first and last digit from each line,
# sum the values
# result should be: 142

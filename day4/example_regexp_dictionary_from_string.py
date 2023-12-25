import re
text = 'red 10, blue 20, white 50, alpha 28'
colors = {}
for m in re.finditer(r'(?P<color>[a-zA-Z]+) (?P<value>\d+)', text):
    print(m.groupdict())
    new_color_dict = m.groupdict()
    colors[new_color_dict["color"]] = int(new_color_dict["value"])

print(colors)

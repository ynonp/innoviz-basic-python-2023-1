import re
import io

demo_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def line_to_list_of_rounds(line: str) -> list[dict[str, int]]:
    _, results = line.split(":")
    rounds = results.split(";")
    result = []
    for round in rounds:
        round_dict = {}
        for pair in re.finditer(r'(\d+) ([a-z]+)', round):
            amount, color = pair.groups()
            round_dict[color] = int(amount)
        result.append(round_dict)
    return result

games = [
    [
        {
            "blue": 3,
            "red": 4
        },
        {
            "red": 1,
            "green": 2,
            "blue": 6
        },
        {
            "green": 2
        }
    ],
    [
        {
            "blue": 1,
            "green": 2,
        },
        {
            "green": 3,
            "blue": 4,
            "red": 1
        },
        {
            "green": 1,
            "blue": 1
        }
    ]
]

results = [line_to_list_of_rounds(line)
    for line in io.StringIO(demo_input)]

print(results[1][1]["red"])
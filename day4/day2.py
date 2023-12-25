text = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
"""

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

print(games[0][1]["red"])

from typing import Literal
from collections import defaultdict
import random
PlayerSign = Literal['x', 'o']
BoardSign = Literal['x', 'o', '.']

class AIPlayer:
    sign: PlayerSign

    def __init__(self, sign: PlayerSign):
        self.sign = sign

    def __str__(self):
        return self.sign

    def get_next_move(self):
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        print(f"AI Playing at {row}, {column}")
        return row, column

class HumanPlayer:
    sign: str

    def __init__(self, sign: str):
        self.sign = sign

    def __str__(self):
        return self.sign

    def get_next_move(self):
        next_move = input("play: (row, column) ")
        row, column = [int(x) for x in next_move.split(",")]
        return row, column


class Game:
    board: list[list[BoardSign]]
    player: HumanPlayer | AIPlayer
    players: list[HumanPlayer | AIPlayer]

    # new object is created
    def __init__(self, players):
        self.board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        self.players = players
        self.player = self.players[0]

    def print(self):
        for row in self.board:
            for square in row:
                print(square, end=" ")
            print()
        print(f"Next player: {self.player}. Go!")

    def play(self):
        self.print()
        row, column = self.player.get_next_move()
        self.board[row][column] = self.player
        self.next_turn()

    def next_turn(self):
        if self.player == self.players[0]:
            self.player = self.players[1]
        else:
            self.player = self.players[0]


games = {'': Game([HumanPlayer('x'), HumanPlayer('o')])}

current_game = games['']
while True:
    try:
        game_name = input("what game do you want to play? ")
        if game_name not in games:
            if game_name.endswith('against_ai'):
                games[game_name] = Game([HumanPlayer('x'), AIPlayer('o')])
            else:
                games[game_name] = Game([HumanPlayer('x'), HumanPlayer('o')])

        current_game = games[game_name]
        current_game.play()
    except ValueError:
        print("Invalid move, please use [row,column] format")
    except IndexError:
        print("The board only has 3x3 squares, please select a place within the board")





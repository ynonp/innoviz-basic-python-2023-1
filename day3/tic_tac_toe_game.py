from collections import defaultdict

class Player:
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
    board: list[list[str]]
    player: Player
    players: list[Player]

    # new object is created
    def __init__(self):
        self.board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        self.players = [Player('x'), Player('o')]
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




games = defaultdict(Game)
current_game = games['default']
while True:
    try:
        game_name = input("what game do you want to play? ")
        if game_name != '':
            current_game = games[game_name]
        current_game.play()
    except ValueError:
        print("Invalid move, please use [row,column] format")
    except IndexError:
        print("The board only has 3x3 squares, please select a place within the board")







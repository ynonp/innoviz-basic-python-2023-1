from collections import defaultdict
class Game:
    board: list[list[str]]
    player: str

    # new object is created
    def __init__(self):
        self.board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        self.player = 'x'

    def print(self):
        for row in self.board:
            for square in row:
                print(square, end=" ")
            print()
        print(f"Next player: {self.player}. Go!")

    def play(self):
        row, column = self.get_next_move()
        self.board[row][column] = self.player
        self.next_turn()

    def next_turn(self):
        if self.player == 'x':
            self.player = 'o'
        else:
            self.player = 'x'

    def get_next_move(self):
        self.print()
        next_move = input("play: (row, column) ")
        row, column = [int(x) for x in next_move.split(",")]
        return row, column


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







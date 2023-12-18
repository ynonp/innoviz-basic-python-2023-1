def new_board():
    return [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ]


def print_board(board: list[list[str]]):
    for row in board:
        for square in row:
            print(square, end=" ")
        print()


def play(board: list[list[str]],
         player: str,
         row: int,
         column: int) -> list[list[str]]:
    board[row][column] = player
    return board


def next_player(player: str) -> str:
    if player == 'x':
        return 'o'
    else:
        return 'x'


game = new_board()
player = 'x'
while True:
    try:
        next_move = input("play: (row, column) ")
        row, column = [int(x) for x in next_move.split(",")]
        play(game, player, row, column)
        print_board(game)
        player = next_player(player)
    except ValueError:
        print("Invalid move, please use [row,column] format")
    except IndexError:
        print("The board only has 3x3 squares, please select a place within the board")







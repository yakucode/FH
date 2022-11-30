import random

board = []
dimension = 5
numOfTries = 10

for x in range(dimension):
    board.append(["0"] * dimension)


def printBoard(board):
    for row in board:
        print(" ".join(row))


def random_row(board):
    return random.randint(0, len(board) - 1)


def random_col(board):
    return random.randint(0, len(board[0]) - 1)


def main():

    printBoard(board)

    ship_row = random_row(board)
    ship_col = random_col(board)

    for turn in range(numOfTries):
        guess_row = int(input("Row: "))
        guess_col = int(input("Column: "))

        if guess_row == ship_row and guess_col == ship_col:
            print("ship sunk!")
            break

        else:
            if turn == numOfTries:
                print("game over")

            elif (guess_row < 0 or guess_row > dimension-1) or (guess_col < 0 or guess_col > dimension-1):
                print("Ups, Du hast noch nicht einmal das Spielfeld getroffen")
            elif (board[guess_row][guess_col] == "X"):
                print("das feld hattest du schon")
            else:
                print("miss")
                board[guess_row][guess_col] == "X"
            print("your turn:", turn+1)
            printBoard(board)


main()

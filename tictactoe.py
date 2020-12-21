def make_matrix(list_, n):
    for i in range(0, len(list_), n):
        yield list_[i:i + n]


def binary_matrix(matrix_):
    for j in range(len(matrix_)):
        for i in range(len(matrix_)):
            if matrix_[i][j] == "X":
                matrix_[i][j] = 1
            elif matrix_[i][j] == "O":
                matrix_[i][j] = -1
            else:
                matrix_[i][j] = 0
    binary_matrix_ = matrix_
    return binary_matrix_


def battle(mtrx):
    winner = []
    # check rows
    for row_ in mtrx:
        if all(x == "X" for x in row_):
            win = "X"
            winner.append(win)
        elif all(x == "O" for x in row_):
            win = "O"
            winner.append(win)

    # check cols
    for j in range(len(mtrx)):
        if all([mtrx[i][j] == "X" for i in range(len(mtrx))]):
            win = "X"
            winner.append(win)
        elif all([mtrx[i][j] == "O" for i in range(len(mtrx))]):
            win = "O"
            winner.append(win)

    # check diag_main
    for x in range(1):
        if all([mtrx[i][i] == "X" for i in range(len(mtrx))]):
            win = "X"
            winner.append(win)
        elif all([mtrx[i][i] == "O" for i in range(len(mtrx))]):
            win = "O"
            winner.append(win)

    # check diag_sec
    for x in range(1):
        if all([mtrx[i][len(mtrx) - i - 1] == "X" for i in range(len(mtrx))]):
            win = "X"
            winner.append(win)
        elif all([mtrx[i][len(mtrx) - i - 1] == "O" for i in range(len(mtrx))]):
            win = "O"
            winner.append(win)

    return winner


def turn(matrix_, row_, col_):
    global turns

    matrix_[row_ - 1][col_ - 1] = turns.pop()

    new_string = []
    for row_ in matrix_:
        for element in row_:
            new_string.append(element)
    return "".join(new_string)


game_string = "_________"
game_list = list(game_string)
display = list(make_matrix(game_list, 3))
turns = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]


while True:

    print("-" * 9)
    for i_ in display:
        print("| " + " ".join(i_) + " |")
    print("-" * 9)

    result = battle(display)
    if any(result):
        print("".join(result) + " wins")
        break
    elif len(turns) == 0:
        print("Draw")
        break

    while True:
        row, col = input("Enter the coordinates: ").split()

        if row.isalpha() or col.isalpha():
            print("You should enter numbers!")

        elif int(row) not in range(1, 4) or int(col) not in range(1, 4):
            print("Coordinates should be from 1 to 3!")

        elif display[int(row) - 1][int(col) - 1] != "_":
            print("This cell is occupied! Choose another one!")

        else:
            break

    game_string = turn(display, int(row), int(col))

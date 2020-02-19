game_running = True
winner = None
current_player = "X"

game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]


def run_game():

    display_board()

    while game_running:
        handle_turn(current_player)
        check_if_game_over()
        change_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


def display_board():
    print("\n")
    print(game_board[0] + " | " + game_board[1] +
          " | " + game_board[2] + "     1 | 2 | 3")
    print(game_board[3] + " | " + game_board[4] +
          " | " + game_board[5] + "     4 | 5 | 6")
    print(game_board[6] + " | " + game_board[7] +
          " | " + game_board[8] + "     7 | 8 | 9")
    print("\n")


def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if game_board[position] == "-":
            valid = True
        else:
            print("Please choose a valid position.")

    game_board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_running

    row_1 = game_board[0] == game_board[1] == game_board[2] != "-"
    row_2 = game_board[3] == game_board[4] == game_board[5] != "-"
    row_3 = game_board[6] == game_board[7] == game_board[8] != "-"

    if row_1 or row_2 or row_3:
        game_running = False

    if row_1:
        return game_board[0]
    elif row_2:
        return game_board[3]
    elif row_3:
        return game_board[6]
    else:
        return None


def check_columns():
    global game_running

    column_1 = game_board[0] == game_board[3] == game_board[6] != "-"
    column_2 = game_board[1] == game_board[4] == game_board[7] != "-"
    column_3 = game_board[2] == game_board[5] == game_board[8] != "-"

    if column_1 or column_2 or column_3:
        game_running = False

    if column_1:
        return game_board[0]
    elif column_2:
        return game_board[1]
    elif column_3:
        return game_board[2]
    else:
        return None


def check_diagonals():
    global game_running
    diagonal_1 = game_board[0] == game_board[4] == game_board[8] != "-"
    diagonal_2 = game_board[2] == game_board[4] == game_board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_running = False

    if diagonal_1:
        return game_board[0]
    elif diagonal_2:
        return game_board[2]
    else:
        return None


def check_for_tie():
    global game_running
    if "-" not in game_board:
        game_running = False
        return True
    else:
        return False


def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


run_game()

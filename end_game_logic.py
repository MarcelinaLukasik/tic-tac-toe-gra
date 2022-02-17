from board_display import show_game


def check_win(board):  # Porównuje czy 3 pola są takie same, ale nie są "?"
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != "?":
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != "?":
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != "?":
        return True
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != "?":
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != "?":
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != "?":
        return True
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != "?":
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != "?":
        return True
    else:
        return False


def check_if_win(board, current_player):
    game_running = True
    if check_win(board):
        show_game(board)
        print("The winner is " + current_player)
        game_running = False
        return game_running
    return game_running


def check_tie(board):
    for row in range(len(board)):
        for element in range(len(board[row])):
            if board[row][element] == "?":
                tie = False
                return tie
    show_game(board)
    print("No winners!")
    tie = True
    return tie

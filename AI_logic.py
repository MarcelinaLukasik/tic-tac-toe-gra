import random
import time
from end_game_logic import check_win
from player_logic import change_player


def AI_1(current_player, game_display):  # Wybiera losowe, wolne miejsce na planszy
    print("Computer turn...")
    while current_player == "O":
        time.sleep(1)
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if game_display[row][col] == "?":
            game_display[row][col] = "O"
            current_player = "X"

    return current_player, game_display


def AI_2(game_display, current_player):  # Dodatkowo sprawdza, czy ruch daje wygraną
    print("Computer turn...")
    while current_player == "O":
        time.sleep(1)
        is_win = False
        for row in range(len(game_display)):
            for element in range(len(game_display[row])):
                if game_display[row][element] == "?":
                    game_display[row][element] = "O"
                    if check_win(game_display):
                        return game_display, current_player
                    else:
                        game_display[row][element] = "?"

        position_taken = False
        while not position_taken:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if game_display[row][column] == "?":
                game_display[row][column] = current_player
                position_taken = True

        current_player = change_player(current_player)

        return game_display, current_player



def AI_3(game_display, current_player, first_time):       # Unbeatable AI, stara się zająć środkowe pole w pierwszym ruchu, blokuje wygraną przeciwnika
    print("Computer turn...")                             # Sprawdza, czy może jakimś ruchem wygrać grę  
    while current_player == "O":
        time.sleep(1)
        if game_display[1][1] == "?":
            game_display[1][1] = "O"
            current_player = change_player(current_player)
            first_time = False
        elif first_time:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if game_display[row][col] == "?":
                game_display[row][col] = "O"
                current_player = change_player(current_player)
                first_time = False
        else:
            for row in range(0, 3):
                for col in range(0, 3):
                    if game_display[row][col] == "?":
                        game_display[row][col] = "O"
                        if check_win(game_display):
                            current_player = change_player(current_player)
                            return game_display, current_player, first_time
                        else:
                            game_display[row][col] = "?"

            for row in range(0, 3):
                for col in range(0, 3):
                    if game_display[row][col] == "?":
                        game_display[row][col] = "X"
                        if check_win(game_display):
                            game_display[row][col] = "O"
                            current_player = change_player(current_player)
                            return game_display, current_player, first_time
                        else:
                            game_display[row][col] = "?"

            game_display = AI_second_move(board=game_display)
            current_player = change_player(current_player)

    return game_display, current_player, first_time


def AI_second_move(board):
    if (board[0][0] == "O" or board[0][1] == "O" or board[0][2] == "O") and (
            board[0][0] != "X" and board[0][1] != "X" and board[0][2] != "X"):
        if board[0][0] == "?":
            board[0][0] = "O"
        elif board[0][1] == "?":
            board[0][1] = "O"
        elif board[0][2] == "?":
            board[0][2] = "O"
    elif (board[1][0] == "O" or board[1][1] == "O" or board[1][2] == "O") and (
            board[1][0] != "X" and board[1][1] != "X" and board[1][2] != "X"):
        if board[1][0] == "?":
            board[1][0] = "O"
        elif board[1][1] == "?":
            board[1][1] = "O"
        elif board[1][2] == "?":
            board[1][2] = "O"
    elif (board[2][0] == "O" or board[2][1] == "O" or board[2][2] == "O") and (
            board[2][0] != "X" and board[2][1] != "X" and board[2][2] != "X"):
        if board[2][0] == "?":
            board[2][0] = "O"
        elif board[2][1] == "?":
            board[2][1] = "O"
        elif board[2][2] == "?":
            board[2][2] = "O"
    elif (board[0][0] == "O" or board[1][0] == "O" or board[2][0] == "O") and (
            board[0][0] != "X" and board[1][0] != "X" and board[2][0] != "X"):
        if board[0][0] == "?":
            board[0][0] = "O"
        elif board[1][0] == "?":
            board[1][0] = "O"
        elif board[2][0] == "?":
            board[2][0] = "O"
    elif (board[0][1] == "O" or board[1][1] == "O" or board[2][1] == "O") and (
            board[0][1] != "X" and board[1][1] != "X" and board[2][1] != "X"):
        if board[0][1] == "?":
            board[0][1] = "O"
        elif board[1][1] == "?":
            board[1][1] = "O"
        elif board[2][1] == "?":
            board[2][1] = "O"
    elif (board[0][2] == "O" or board[1][2] == "O" or board[2][2] == "O") and (
            board[0][2] != "X" and board[1][2] != "X" and board[2][2] != "X"):
        if board[0][2] == "?":
            board[0][2] = "O"
        elif board[1][2] == "?":
            board[1][2] = "O"
        elif board[2][2] == "?":
            board[2][2] = "O"
    elif (board[0][0] == "O" or board[1][1] == "O" or board[2][2] == "O") and (
            board[0][0] != "X" and board[1][1] != "X" and board[2][2] != "X"):
        if board[0][0] == "?":
            board[0][0] = "O"
        elif board[1][1] == "?":
            board[1][1] = "O"
        elif board[2][2] == "?":
            board[2][2] = "O"
    elif (board[0][2] == "O" or board[1][1] == "O" or board[2][0] == "O") and (
            board[0][2] != "X" and board[1][1] != "X" and board[2][0] != "X"):
        if board[0][2] == "?":
            board[0][2] = "O"
        elif board[1][1] == "?":
            board[1][1] = "O"
        elif board[2][0] == "?":
            board[2][0] = "O"
    else:
        for row in range(0, 3):
            for col in range(0, 3):
                if board[row][col] == "?":
                    board[row][col] = "O"
                    break
    return board

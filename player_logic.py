def change_player(current_player):
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    return current_player

def input_for_players(board, current_player):
    valid_input_0 = False
    valid_input_1 = False
    free_place = False
    while not (valid_input_0 and valid_input_1 and free_place):
        player_input = input("Choose row and column: ").upper()
        if len(player_input) == 2:
            if player_input[0] == "A":
                valid_input_0 = True
            elif player_input[0] == "B":
                valid_input_0 = True
            elif player_input[0] == "C":
                valid_input_0 = True
            else:
                break
            if player_input[1] == "1":
                valid_input_1 = True
            elif player_input[1] == "2":
                valid_input_1 = True
            elif player_input[1] == "3":
                valid_input_1 = True
            else:
                break
        else:
            break

        player_input_row = player_input[0]
        player_input_column = int(player_input[1])

        if player_input_row == "A":
            player_input_row = 1
        elif player_input_row == "B":
            player_input_row = 2
        elif player_input_row == "C":
            player_input_row = 3
        

        if board[player_input_row - 1][player_input_column - 1] == "?":
            board[player_input_row - 1][player_input_column - 1] = current_player
            free_place = True
        else:
            print("Place is already taken, choose a different one!")
            free_place = False

    return board, current_player

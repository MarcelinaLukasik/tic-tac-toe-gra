def change_player(current_player):
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return current_player

def get_human_coordinates(board, current_player):
    valid_input = False
    free_place = False
    while not (valid_input and free_place):
        player_input = input("Choose row and column:\n").upper()
        if len(player_input) == 2 and player_input[0] in 'ABC' and player_input[1] in '123':
            valid_input = True
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
        else:
            print("Wrong coordinates, provide other ones!")


    return board, current_player

import random
import time

def AI(current_player, game_display):                                   # Wybiera losowe, wolne miejsce na planszy
    while current_player == "O":
        # print("Computer turn...")
        time.sleep(1)
        # for row in range(len(game_display)):
        row = random.randint(0,2)
        # for column in range(len(game_display[row])):
        column = random.randint(0,2)
        if game_display[row][column] == "?":
            game_display[row][column] = current_player
            current_player = "X"
    return game_display, current_player
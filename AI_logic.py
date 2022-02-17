import random
import time

def AI(current_player, game_display):                                   # Wybiera losowe, wolne miejsce na planszy
    while current_player == "O":
        print("Computer turn...")
        time.sleep(1)
        position = random.randint(0, 8)
        if game_display[position] == "?":
            game_display[position] = "O"
            # change_player()
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
            return current_player, game_display
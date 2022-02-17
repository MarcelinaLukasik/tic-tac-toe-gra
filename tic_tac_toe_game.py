import keyboard
from game_init import initialize_game
from game_engine import game_start

def main():
    print("Press enter to play or 'q' to exit ")
    new_game = True
    while new_game:
        if keyboard.read_key() == "q":
            print("BYE BYE")
            new_game = False

        elif keyboard.is_pressed("\n"):
            input()
            game_display, game_running, current_player, first_time = initialize_game()
            game_start(game_display, game_running, current_player, first_time)

if __name__ == "__main__":
    main()

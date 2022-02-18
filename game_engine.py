from board_display import show_game
from end_game_logic import check_if_win, check_win, check_tie
from player_logic import get_human_coordinates, change_player
from modes import pvp_mode, AI_mode_1, AI_mode_2, AI_mode_3


def game_start(game_display, game_running, current_player, first_time):
    player_input = (
        input("Choose game mode: 1 - player vs player, 2 - player vs AI (random), 3 - player vs AI (goes for easy win), 4 - Unbeatable AI: "))
    while game_running:
        if player_input == "1":
            game_display, current_player, game_running = pvp_mode(game_display, current_player)
            
        elif player_input == "2":
            game_display, current_player, game_running = AI_mode_1(game_display, current_player)

        elif player_input == "3":
            game_display, current_player, game_running = AI_mode_2(game_display, current_player, game_running)

        elif player_input == "4":
            game_display, current_player, game_running, first_time = AI_mode_3(game_display, current_player, first_time, game_running)

    print(" THE END")
    print("Press enter to play or 'q' to exit ")

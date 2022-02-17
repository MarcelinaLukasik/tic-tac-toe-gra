from AI_logic import AI_1, AI_2, AI_3
from board_display import show_game
from end_game_logic import check_if_win, check_win, check_tie
from player_logic import input_for_players, change_player


def game_start(game_display, game_running, current_player, first_time):
    player_input = (
        input("Choose game mode: 1 - player vs player, 2 - player vs AI easy, 3 - player vs AI medium, 4 - AI hard "))
    while game_running:
        if player_input == "1":
            show_game(game_display)
            board, current_player = input_for_players(game_display, current_player)
            game_running = check_if_win(game_display, current_player)
            if check_tie(game_display):
                game_running = False
            current_player = change_player(current_player)

        elif player_input == "2":
            show_game(game_display)
            board, current_player = input_for_players(game_display, current_player)
            game_running = check_if_win(game_display, current_player)
            if check_tie(game_display):
                game_running = False
            show_game(game_display)
            current_player = change_player(current_player)
            current_player, game_display = AI_1(current_player, game_display)
            game_running = check_if_win(game_display, current_player)
            if check_tie(game_display):
                game_running = False

        elif player_input == "3":
            show_game(game_display)
            board, current_player = input_for_players(game_display, current_player)
            show_game(game_display)
            if check_win(game_display):
                game_running = check_if_win(game_display, current_player)
                break
            if check_tie(game_display):
                game_running = False
            current_player = change_player(current_player)
            game_display, current_player = AI_2(game_display, current_player)
            if check_win(game_display):
                game_running = check_if_win(game_display, current_player)
            if check_tie(game_display):
                game_running = False

        elif player_input == "4":
            show_game(game_display)
            board, current_player = input_for_players(game_display, current_player)
            show_game(game_display)
            if check_win(game_display):
                game_running = check_if_win(game_display, current_player)
                break
            if check_tie(game_display):
                game_running = False
            current_player = change_player(current_player)
            game_display, current_player, first_time = AI_3(game_display, current_player, first_time)
            if check_win(game_display):
                current_player = change_player(current_player)
                game_running = check_if_win(game_display, current_player)
            if check_tie(game_display):
                game_running = False

    print(" THE END")
    print("Press enter to play or 'q' to exit ")

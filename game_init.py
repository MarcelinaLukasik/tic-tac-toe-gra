def initialize_game():
    game_display = [["?"] * 3 for n in range(3)]
    game_running = True
    current_player = "X"
    first_time = True

    return game_display, game_running, current_player, first_time


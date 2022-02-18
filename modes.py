from board_display import show_game
from player_logic import get_human_coordinates, change_player
from end_game_logic import check_if_win, check_tie, check_win
from AI_logic import AI_1, AI_2, AI_3

def pvp_mode(game_display, current_player):
    show_game(game_display)
    game_display, current_player = get_human_coordinates(game_display, current_player)
    game_running = check_if_win(game_display, current_player)
    if check_tie(game_display):
        game_running = False
    current_player = change_player(current_player)
    return game_display, current_player, game_running

def AI_mode_1(game_display, current_player):
    show_game(game_display)
    game_display, current_player = get_human_coordinates(game_display, current_player)
    if check_win(game_display):
        game_running = check_if_win(game_display, current_player)
        return game_display, current_player, game_running
    if check_tie(game_display):
        game_running = False
        return game_display, current_player, game_running
    show_game(game_display)
    current_player = change_player(current_player)
    current_player, game_display, winner= AI_1(current_player, game_display)
    game_running = check_if_win(game_display, winner)
    if check_tie(game_display):
        game_running = False
        return game_display, current_player, game_running
    return game_display, current_player, game_running

def AI_mode_2(game_display, current_player, game_running):
    show_game(game_display)
    game_display, current_player = get_human_coordinates(game_display, current_player)
    show_game(game_display)
    if check_win(game_display):
        game_running = check_if_win(game_display, current_player)
        return game_display, current_player, game_running
    if check_tie(game_display):
        game_running = False
        return game_display, current_player, game_running
    current_player = change_player(current_player)
    game_display, current_player = AI_2(game_display, current_player)
    if check_win(game_display):
        game_running = check_if_win(game_display, current_player)
        return game_display, current_player, game_running
    if check_tie(game_display):
        game_running = False
        return game_display, current_player, game_running
    return game_display, current_player, game_running

def AI_mode_3(game_display, current_player, first_time, game_running):
    show_game(game_display)
    game_display, current_player = get_human_coordinates(game_display, current_player)
    show_game(game_display)
    if check_win(game_display):
        game_running = check_if_win(game_display, current_player)
        return game_display, current_player, game_running, first_time
    if check_tie(game_display):
        game_running = False
        return game_display, current_player, game_running, first_time
    current_player = change_player(current_player)
    game_display, current_player, first_time = AI_3(game_display, current_player, first_time)
    if check_win(game_display):
        current_player = change_player(current_player)
        game_running = check_if_win(game_display, current_player)
        return game_display, current_player, game_running, first_time
    if check_tie(game_display):
        game_running = False
        return game_display, current_player, game_running, first_time
    return game_display, current_player, game_running, first_time
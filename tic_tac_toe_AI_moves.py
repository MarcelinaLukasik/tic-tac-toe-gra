def AI_check_moves(board):
    if (board[0] == "O" or board[1] == "O" or board[2] == "O") and (board[0] != "X" and board[1] != "X" and board[2] != "X"):
        if board[0] == "?":
            board[0] = "O" 
        elif board[1] == "?":
            board[1] = "O"
        elif board[2] == "?":
            board[2] = "O"
    elif (board[3] == "O" or board[4] == "O" or board[5] == "O") and (board[3] != "X" and board[4] != "X" and board[5] != "X"):
        if board[3] == "?":
            board[3] = "O" 
        elif board[4] == "?":
            board[4] = "O"
        elif board[5] == "?":
            board[5] = "O"
    elif (board[6] == "O" or board[7] == "O" or board[8] == "O") and (board[6] != "X" and board[7] != "X" and board[8] != "X"):
        if board[6] == "?":
            board[6] = "O" 
        elif board[7] == "?":
            board[7] = "O"
        elif board[8] == "?":
            board[8] = "O"
    elif (board[0] == "O" or board[3] == "O" or board[6] == "O") and (board[0] != "X" and board[3] != "X" and board[6] != "X"):
        if board[0] == "?":
            board[0] = "O" 
        elif board[3] == "?":
            board[3] = "O"
        elif board[6] == "?":
            board[6] = "O"
    elif (board[1] == "O" or board[4] == "O" or board[7] == "O") and (board[1] != "X" and board[4] != "X" and board[7] != "X"):
        if board[1] == "?":
            board[1] = "O" 
        elif board[4] == "?":
            board[4] = "O"
        elif board[7] == "?":
            board[7] = "O"
    elif (board[2] == "O" or board[5] == "O" or board[8] == "O") and (board[2] != "X" and board[5] != "X" and board[8] != "X"):
        if board[2] == "?":
            board[2] = "O" 
        elif board[5] == "?":
            board[5] = "O"
        elif board[8] == "?":
            board[8] = "O"
    elif (board[0] == "O" or board[4] == "O" or board[8] == "O") and (board[0] != "X" and board[4] != "X" and board[8] != "X"):
        if board[0] == "?":
            board[0] = "O" 
        elif board[4] == "?":
            board[4] = "O"
        elif board[8] == "?":
            board[8] = "O"
    elif (board[2] == "O" or board[4] == "O" or board[6] == "O") and (board[2] != "X" and board[4] != "X" and board[6] != "X"):
        if board[2] == "?":
            board[2] = "O" 
        elif board[4] == "?":
            board[4] = "O"
        elif board[6] == "?":
            board[6] = "O"
    else:
        for position in range(0,9):   
           if board[position] == "?":
                board[position] = "O"
                break
    return board
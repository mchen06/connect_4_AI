def player_Miley(board, player):
    
    def has_won(board, player):
        if check_horozontal(board, player) == 1:
            return 1
        if check_vertical(board, player) == 1:
            return 1
        if check_diagonal(board, player) == 1:
            return 1
        if check_diagonal_inverse(board, player) == 1:
            return 1
        else:
            return -1

    def check_horozontal(board, player):
        for row in range(0, 8):
            for col in range(0, 6):
                if board[col][row] == player and board[col + 1][row] == player and board[col + 2][row] == player and board[col + 3][row] == player:
                    return 1
            
    def check_vertical(board, player):
        for col in range(0, 9):
            for row in range(0, 5):
                if board[col][row] == player and board[col][row + 1] == player and board[col][row + 2] == player and board[col][row + 3] == player:
                   return 1
    
    def check_diagonal(board, player):
        for col in range(0, 6):
            for row in range(2, 8):
                if board[col][row] == player and board[col + 1][row - 1] == player and board[col + 2][row - 2] == player and board[col + 3][row - 3] == player:
                    return 1
            
    def check_diagonal_inverse(board, player):
        for col in range(0, 7):
            for row in range(0, 6):
                if board[col][row] == player and board[col + 1][row + 1] == player and board[col + 2][row + 2] == player and board[col + 3][row + 3] == player:
                    return 1

    def random_move(board, player, other_player):
        import random
        columns = [0, 1, 2, 3, 5, 6, 7, 8]
        move_a = random.choices(columns, weights=(2, 11, 15, 25, 25, 15, 11, 2), k = 1)
        move_b = ''.join(str(e) for e in move_a)
        move_c = int(move_b)
        if board[4][7] == 0 and does_move_make_lose(board, player, other_player, 4) <= 0:
           return 4
        if make_3_in_a_row(board, player) >= 0:
            if does_move_make_lose(board, player, other_player, make_3_in_a_row(board, player)) <= 0:
                return make_3_in_a_row(board, player)
        if make_3_in_a_row(board, other_player) >= 0:
            if does_move_make_lose(board, player, other_player, make_3_in_a_row(board, other_player)) <= 0:
                return make_3_in_a_row(board, other_player)
        if does_move_make_lose(board, player, other_player, move_c) >= 0:
            return if_move_makes_lose(flipped_board, player, other_player, move_c)
        else:
            return move_c

    def flip_board(board):
        from copy import copy, deepcopy
        board_copy = deepcopy(board)
        flip_board = []
        for col in board_copy:
            col.reverse()
            flip_board.append(col)
        return flip_board
        
    def new_board(board, player, column):
        from copy import copy, deepcopy
        board_copy = deepcopy(board)
        for row in range(0, 8):
            if (board_copy[column][row]) == 0: 
                (board_copy[column][row]) = player
                break
        return board_copy

    def best_column(board, player):
        for x in range(0, 9):
            board_copy = new_board(board, player, x) 
            if has_won (board_copy, player) == True:
                if board_copy[x][7] == 0:
                    return x
        return -1

    def does_move_make_lose(board, player, other_player, column):
        from copy import copy, deepcopy
        board_copy = deepcopy(new_board(board, player, column))
        board_copy = new_board(board_copy, other_player, best_column(board_copy, other_player))
        return has_won(board_copy, other_player)

    def if_move_makes_lose(board, player, other_player, move_c):
        if does_move_make_lose(flipped_board, player, other_player, move_c) == True:
            columns.remove(move_c)
            column_decision = random.choices(columns, weights=(2, 8, 25, 30, 25, 8, 2), k = 1)
            columns = [0, 1, 2, 3, 5, 6, 7, 8]
            column_decision_a = ''.join(str(e) for e in column_decision)
            column_decision_b = int(column_decision_a)
            return column_decision_b
        else:
            return -1

    def three_in_a_row(board, player):
        for row in range(0, 7):
           for col in range(0, 6):
                if board[col][row] == player and board[col + 1][row] == player and board[col + 2][row] == 0:
                    if row == 0:
                        return col + 2
                    if board[col + 2][row - 1] != 0 or board[col + 2][0] == 0:
                        return col + 2
        for row in range(0, 7):
            for col in range(2, 8):
                if board[col][row] == player and board[col - 1][row] == player and board[col - 2][row] == 0:
                    if row == 0:
                        return col -2
                    if board[col - 2][row - 1] != 0 or board[col - 2][0] == 0:
                        return col - 2
        for row in range(0, 7):
            for col in range(0, 6):
                if board[col][row] == player and board[col + 2][row] == player and board[col + 1][row] == 0:
                    if board[col + 1][row - 1] != 0 or board[col + 1][0] == 0:
                        return col + 1
        return -1

    def make_3_in_a_row(board, player):
        if make_3_in_a_row_horozontal(board, player) >= 0:
            return make_3_in_a_row_horozontal(board, player)
        if make_3_in_a_row_vertical(board, player) >= 0:
            return make_3_in_a_row_vertical(board, player)
        if make_3_in_a_row_diagonal(board, player) >= 0:
            return make_3_in_a_row_diagonal(board, player)
        if make_3_in_a_row_diagonal_inverse (board, player) >= 0:
            return make_3_in_a_row_diagonal_inverse (board, player) >= 0        
        for col in range(0, 7):
            for row in range(0, 6):
                if board[col][row] == player and board[col + 1][row + 1] == player and board[col + 2][row + 2] == 0:
                    if board[col + 2][row + 1] != 0:
                        return col + 2
        return -1

    def make_3_in_a_row_horozontal(board, player):
        for row in range(0, 8):
            for col in range(0, 7):
                if board[col][row] == player and board[col + 1][row] == player and board[col + 2][row] == 0:
                    if board[col + 2][row - 1] != 0 or board[col + 1][0] == 0:
                        return col + 2
        for row in range(0, 8):
            for col in range(0, 7):
                if board[col][row] == player and board[col + 1][row] == 0 and board[col + 2][row] == player:
                    if board[col + 1][row - 1] != 0 or board[col + 1][0] == 0:
                        return col + 1
        for row in range(0, 8):
            for col in range(0, 7):
                if board[col][row] == 0 and board[col + 1][row] == player and board[col + 2][row] == player:
                    if board[col][row - 1] != 0 or board[col][0] == 0:
                        return col
        return -1 

    def make_3_in_a_row_vertical (board, player):
        for col in range(0, 9):
            for row in range(0, 6):
                if board[col][row] == player and board[col][row + 1] == player and board[col][row + 2] == 0:
                    if board[col][row + 1] != 0:
                       return col
        return -1 

    def make_3_in_a_row_diagonal (board, player):
        for col in range(0, 7):
            for row in range(2, 8):
                if board[col][row] == player and board[col + 1][row - 1] == player and board[col + 2][row - 2] == 0:
                    if board[col + 2][row - 3] != 0 or board[col + 2][0] == 0:
                        return col + 2
        for col in range(0, 7):
            for row in range(2, 8):
                if board[col][row] == player and board[col + 1][row - 1] == 0 and board[col + 2][row - 2] == player:
                    if board[col + 1][row - 2] != 0 or board[col + 1][0] == 0:
                        return col + 1
        for col in range(0, 7):
            for row in range(2, 8):
                if board[col][row] == 0 and board[col + 1][row - 1] == player and board[col + 2][row - 2] == player:
                    if board[col + 2][row - 1] != 0 or board[col][0] == 0:
                        return col
        return -1

    def make_3_in_a_row_diagonal_inverse (board, player):
        for col in range(0, 7):
            for row in range(0, 6):
                if board[col][row] == player and board[col + 1][row + 1] == player and board[col + 2][row + 2] == 0:
                    if board[col + 2][row + 1] != 0:
                        return col + 2
        for col in range(0, 7):
            for row in range(0, 6):
                if board[col][row] == player and board[col + 1][row + 1] == 0 and board[col + 2][row + 2] == player:
                    if board[col + 1][row] != 0:
                        return col + 1
        for col in range(0, 7):
            for row in range(0, 6):
                if board[col][row] == 0 and board[col + 1][row + 1] == player and board[col + 2][row + 2] == player:
                    if board[col][row - 1] != 0 or board[col][row] == 0:
                        return col
        return -1
    
    flipped_board = flip_board(board)
    if player == 1:
        other_player = 2
    if player == 2:
        other_player = 1

    if best_column(flipped_board, player) >= 0:
        return best_column(flipped_board, player)
    if best_column(flipped_board, other_player) >= 0:
        return best_column(flipped_board, other_player)

    if three_in_a_row(flipped_board, player) >= 0:
        if does_move_make_lose(flipped_board, player, other_player, three_in_a_row(flipped_board, player)) >= 0:
            return random_move(flipped_board, player, other_player)
        return three_in_a_row(flipped_board, player)
    
    if three_in_a_row(flipped_board, other_player) >= 0:
        if does_move_make_lose(flipped_board, player, other_player, three_in_a_row(flipped_board, other_player)) >= 0:
            return random_move(flipped_board, player, other_player)
        return three_in_a_row(flipped_board, other_player)

    else:
        return random_move(flipped_board, player, other_player)

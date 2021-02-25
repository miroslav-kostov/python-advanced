def dangerous_rows(king_posish, board):
    kings_row = king_posish[0]
    dangerous = False
    for i in range(king_posish[1], -1, -1):   # LEFT MOVING
        if board[kings_row][i] == "Q":
            print([kings_row, i])
            dangerous = True
            break

    for i in range(king_posish[1], 8):   # RIGHT MOVING
        if board[kings_row][i] == "Q":
            print([kings_row, i])
            dangerous = True
            break

    return dangerous


def dangerous_column(k_posish, board):
    kings_col = k_posish[1]
    dangerous = False
    for i in range(k_posish[0], 8):
        if board[i][kings_col] == "Q":
            print([i, kings_col])
            dangerous = True
            break

    for i in range(k_posish[0], -1, -1):
        if board[i][kings_col] == "Q":
            print([i, kings_col])
            dangerous = True
            break

    return dangerous


def dangerous_diagonals(k_pos, board):
    dangerous = False

    len_bot_right_diagonal = min(7 - k_pos[1], 7 - k_pos[0])  # DIAGONAL 1 / 4 (bot right)

    current_k_pos = [k_pos[0], k_pos[1]]
    for i in range(len_bot_right_diagonal):
        current_k_pos = [x + 1 for x in current_k_pos]
        if board[current_k_pos[0]][current_k_pos[1]] == "Q":
            print([current_k_pos[0], current_k_pos[1]])
            dangerous = True
            break

    len_bot_left_diagonal = min(7 - k_pos[0], k_pos[1])  # DIAGONAL 2 / 4 (bot left)

    current_k_pos = [k_pos[0], k_pos[1]]
    for i in range(len_bot_left_diagonal):
        current_k_pos = [current_k_pos[0]+1, current_k_pos[1]-1]
        if board[current_k_pos[0]][current_k_pos[1]] == "Q":
            print([current_k_pos[0], current_k_pos[1]])
            dangerous = True
            break

    len_top_left_diagonal = min(k_pos[0], k_pos[1])  # DIAGONAL 3 / 4 (top left)

    current_k_pos = [k_pos[0], k_pos[1]]
    for i in range(len_top_left_diagonal):
        current_k_pos = [current_k_pos[0] - 1, current_k_pos[1] - 1]
        if board[current_k_pos[0]][current_k_pos[1]] == "Q":
            print([current_k_pos[0], current_k_pos[1]])
            dangerous = True
            break

    len_bot_left_diagonal = min(k_pos[0], 7 - k_pos[1])  # DIAGONAL 4 / 4 (top right)

    current_k_pos = [k_pos[0], k_pos[1]]
    for i in range(len_bot_left_diagonal):
        current_k_pos = [current_k_pos[0] - 1, current_k_pos[1] + 1]
        if board[current_k_pos[0]][current_k_pos[1]] == "Q":
            print([current_k_pos[0], current_k_pos[1]])
            dangerous = True
            break

    return dangerous


chess_board = []
kings_position = []
queens = {}
current_queen = 0

for row in range(8):
    current_row = input().split()
    chess_board.append(current_row)
    if "K" in current_row:
        kings_column = [x for x in range(len(current_row)) if current_row[x] == "K"]
        kings_position = [row, *kings_column]
    if "Q" in current_row:
        for x in range(len(current_row)):
            if current_row[x] == "Q":
                queens[f"Q{current_queen}"] = [row, x]
                current_queen += 1

is_it_dangerous = [dangerous_rows(kings_position, chess_board), \
                   dangerous_column(kings_position, chess_board), \
                   dangerous_diagonals(kings_position, chess_board)]

if not any(is_it_dangerous):
    print("The king is safe!")

# Chess is the oldest game, but it is still popular these days. For this task,
# we will use only one chess piece - the Knight.
# The knight moves to the nearest square but not on the same row, column, or diagonal. (This can be thought of as
# moving two squares horizontally, then one square vertically, or moving one square horizontally then two squares
# vertically - i.e. in an "L" pattern.)
# The knight game is played on a board with dimensions N x N.
# You will receive a board with K for knights and '0' for empty cells. Your task is to remove knights until there are no
# knights left that can attack one another.

# Input
# - On the first line, you will receive the N size of the board
# - On the next N lines, you will receive strings with Ks and 0s.

# Output
# Print a single integer with the minimum number of knights that needs to be removed

# Constraints
#  The size of the board will be 0 < N < 30
#  Time limit: 0.3 sec. Memory limit: 16 MB.

n = int(input())
matrix = []
for row in range(n):
    matrix.append(list(input()))

def is_valid_bound(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def caluclate_kills(matrix, row, col):
    kills = 0
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for index in range(len(rows)):
        potential_row = row+rows[index]
        potential_col = col+cols[index]
        if is_valid_bound(potential_row, potential_col):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == "K":
                kills += 1
    return kills


removed_knights = 0

while True:
    max_kills = 0
    killer_position = []

    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == "K":
                kills = caluclate_kills(matrix, row_index, col_index)
                if max_kills < kills:
                    max_kills = kills
                    killer_position = [row_index, col_index]

    if killer_position:
        matrix[killer_position[0]][killer_position[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
rows, collumns = map(int, input().split(" "))

def read_matrix():
    result = []
    for row in range(rows):
        result.append(input().split())
    return result


def find_squares(matrix):
    coll_to_check = collumns - 1
    rows_to_check = rows - 1
    squares_found = 0
    for r in range(rows_to_check):
        for c in range(coll_to_check):
            letter = matrix[r][c]
            if letter == matrix[r][c+1] and letter == matrix[r+1][c] and letter == matrix[r+1][c+1]:
                squares_found += 1
    return squares_found


    pass


the_matrix = read_matrix()
print(find_squares(the_matrix))

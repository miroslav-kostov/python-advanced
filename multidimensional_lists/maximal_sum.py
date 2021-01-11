rows, collumns = map(int, input().split(" "))

def init_matrix():
    result = []
    for row in range(rows):
        result.append(list(map(int, input().split())))
    return result


def find_max_sum(matrix):
    max_sum = -2**31-1
    max_matrix = []

    for r in range(rows - 2):
        current_sum = -2**31-1
        for c in range(collumns - 2):
            current_sum = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] + matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+1][c+2] + matrix[r+2][c] + matrix[r+2][c+1] + matrix[r+2][c+2]
            if current_sum > max_sum:
                max_sum = current_sum
                max_matrix = [matrix[r][c], matrix[r][c+1], matrix[r][c+2]], [matrix[r+1][c], matrix[r+1][c+1], matrix[r+1][c+2]], [matrix[r+2][c], matrix[r+2][c+1], matrix[r+2][c+2]]

    print(f"Sum = {max_sum}")
    for i in range(len(max_matrix)):
        for y in range(len(max_matrix[i])):
            max_matrix[i][y] = str(max_matrix[i][y])
        b = " ".join(max_matrix[i])
        print(b)



the_matrix = init_matrix()
find_max_sum(the_matrix)
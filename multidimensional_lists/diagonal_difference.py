def read_matrix():
    size = int(input())
    result = []
    for _ in range(size):
        data = list(map(int, input().split(" ")))
        result.append(data)
    return result

def sum_diagonals(matrix):
    size = len(matrix)
    size_backwards = size
    diagonal_a = 0
    diagonal_b = 0
    for i in range(size):
        diagonal_a += matrix[i][i]
        diagonal_b += matrix[i][size_backwards - 1]
        size_backwards -= 1
    result = abs(diagonal_a - diagonal_b)
    return result


the_matrix = read_matrix()
print(sum_diagonals(the_matrix))
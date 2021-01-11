def read_matrix():
    size = int(input())
    result = []
    for row in range(size):
        row = list(map(int, input().split()))
        result.append(row)
    return result

matrix = read_matrix()
sum_diagonal = 0

for i in range(len(matrix[0])):
    sum_diagonal += matrix[i][i]

print(sum_diagonal)
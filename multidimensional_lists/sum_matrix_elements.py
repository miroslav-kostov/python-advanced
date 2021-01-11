row_matrix, column_matrix = map(int, input().split(", "))
matrix = []
total = 0

for data in range(row_matrix):
    command = list(map(int, input().split(", ")))
    matrix.append(command)

for row in matrix:
    total += sum(row)

print(total)
print(matrix)

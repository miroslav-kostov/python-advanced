def read_matrix():
    row_matrix, column_matrix = map(int, input().split(", "))
    result = []
    for row in range(row_matrix):
        data = list(map(int, input().split(" ")))
        result.append(data)

    return result

matrix = read_matrix()
sums_of_columns = []

for i in range(len(matrix[0])):
    current_collumn = 0
    for row in matrix:
        current_collumn += row[i]
    sums_of_columns.append(current_collumn)


for i in sums_of_columns:
    print(i)
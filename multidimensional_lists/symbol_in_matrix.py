def read_matrix():
    size = int(input())
    result = []
    for _ in range(size):
        result.append([i for i in input()])
    return result


matrix = read_matrix()
symbol = input()
location = None
found = False

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == symbol:
            location = f"({row}, {column})"
            found = True
            break
    if found:
        break

if not location:
    print(f"{symbol} does not occur in the matrix")
else:
    print(location)

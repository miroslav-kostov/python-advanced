matrix = []
for _ in range(int(input())):
    matrix.append(list(map(int, input().split())))

while True:
    command = input()
    if command == "END":
        break
    comm, row, col, value = command.split()
    if int(row) >= len(matrix) or int(col) >= len(matrix) or int(row) < 0 or int(col) < 0:
        print("Invalid coordinates")
    elif comm == "Add":
        matrix[int(row)][int(col)] += int(value)
    elif comm == "Subtract":
        matrix[int(row)][int(col)] -= int(value)

for row in matrix:
    for idx in range(len(row)):
        row[idx] = str(row[idx])
    print(" ".join(row))
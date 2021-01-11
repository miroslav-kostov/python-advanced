matrix = []
for _ in range(int(input())):
    matrix.append(list(map(int, input().split(", "))))

first_diagonal, second_diagonal, size = [], [], int(len(matrix) - 1)

for x in range(len(matrix)):
    first_diagonal.append(matrix[x][x])
    second_diagonal.append(matrix[x][size])
    size -= 1

print(f"First diagonal: {', '.join([str(y) for y in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join([str(y) for y in second_diagonal])}. Sum: {sum(second_diagonal)}")
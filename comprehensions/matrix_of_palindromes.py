rows, cols = map(int, input().split())
matrix = [["x"]*cols for x in range(rows)]
start = 97

for row in range(rows):
    mid_char = start
    for col in range(cols):
        matrix[row][col] = f"{chr(start)}{chr(mid_char)}{chr(start)}"
        mid_char += 1
    start += 1

[print(*row) for row in matrix]
# Write a program that receives a matrix and prints the flattened version of it (a list with all the values).
# For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].

# 3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99

print([x for row in [map(int, input().split(", ")) for _ in range(int(input()))] for x in row])

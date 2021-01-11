size = int(input())
matrix = [map(int, input().split(", ")) for _ in range(size)]
print([[x for x in row if x % 2 == 0] for row in matrix])

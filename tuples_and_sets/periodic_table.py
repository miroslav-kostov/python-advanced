n = int(input())
elements = set()

for _ in range(n):
    compound = input().split()
    for i in compound:
        elements.add(i)

for x in elements:
    print(x)
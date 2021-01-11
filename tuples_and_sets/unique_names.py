total = int(input())
names = []
for _ in range(total):
    names.append(input())

names = set(names)
for name in names:
    print(name)
line = input()
strings = []
for i in line:
    strings.append(i)
while strings:
    print(f"{strings.pop()}", end="")
from collections import deque

liters = int(input())
queue = deque()

command = input()
while command != "Start":
    queue.append(command)
    command = input()

while command != "End":
    if command == "Start":
        command = input()
        continue
    idx = command.split(" ")
    if idx[0] == "refill":
        liters += int(idx[1])
    else:
        if int(idx[0]) <= liters:
            print(f"{queue.popleft()} got water")
            liters -= int(idx[0])
        else:
            print(f"{queue.popleft()} must wait")
    command = input()

print(f"{liters} liters left")
from collections import deque

food_quantity = int(input())
queue = deque(input().split(" "))
length = len(queue)
complete = True

for i in range(length):
    if queue[0].isnumeric():
        queue.append(int(queue.popleft()))
    else:
        queue.popleft()
max_order = max(queue)
print(max_order)
for b in range(length):
    if food_quantity >= queue[0]:
        food_quantity -= queue.popleft()
    else:
        length = len(queue)
        for i in range(length):
            queue.append(str(queue.popleft()))
        print(f"Orders left: {' '.join(queue)}")
        complete = False
        break

if complete:
    print("Orders complete")


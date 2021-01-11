delivery = list(map(int, input().split(" ")))
rack_capacity = int(input())
current_box = rack_capacity
boxes = 0

while delivery:
    if int(delivery[-1]) <= current_box:
        current_box -= int(delivery[-1])
        delivery.pop()
        if not delivery:
            boxes += 1
    else:
        boxes += 1
        current_box = rack_capacity


print(boxes)
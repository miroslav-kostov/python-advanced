n = int(input())
cars = set()
out_cars = set()
for _ in range(n):
    command, current_car = input().split(', ')
    if command == "IN":
        cars.add(current_car)
    elif command == "OUT":
        cars.remove(current_car)
if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
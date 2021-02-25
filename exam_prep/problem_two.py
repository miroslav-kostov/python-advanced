lost = False
won = False

player_location = []
my_path = []
total_coins = 0

movements = {
    "up": [-1, 0],
    "down": [+1, 0],
    "left": [0, -1],
    "right": [0, +1]
}

size_of_field = int(input())
field = []
for i in range(size_of_field):
    current_row = input().split()
    field.append(current_row)
    if "P" in current_row:
        player_location = [i, current_row.index("P")]

while True:
    command = input()
    new_position = [player_location[0] + movements[command][0], player_location[1] + movements[command][1]]
    if new_position[0] < 0 or new_position[0] > size_of_field-1 or new_position[1] < 0 or new_position[0] > size_of_field-1:
        lost = True
        break
    if field[new_position[0]][new_position[1]] == "x" or field[new_position[0]][new_position[1]] == "X":
        lost = True
        break
    my_path.append(new_position)
    if field[new_position[0]][new_position[1]].isnumeric():
        total_coins += int(field[new_position[0]][new_position[1]])
    player_location = [new_position[0], new_position[1]]
    if total_coins >= 100:
        won = True
        break

if won:
    print(f"You won! You've collected {total_coins} coins.")
elif lost:
    total_coins = total_coins // 2
    print(f"Game over! You've collected {total_coins} coins.")
print("Your path:")
for step in my_path:
    print(step)
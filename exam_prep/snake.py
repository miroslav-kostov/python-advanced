size = int(input())
territory = []
current_position = []
food_eaten = 0


def new_position(direction):
    position = [0, 0]
    if direction == "up":
        position = [-1, 0]
    elif direction == "down":
        position = [+1, 0]
    elif direction == "left":
        position = [0, -1]
    elif direction == "right":
        position = [0, +1]
    return position


def position_is_valid(terit, current_posit, new_posit):
    if len(terit) - 1 < (current_posit[0] + new_posit[0]) or \
       len(terit) - 1 < (current_posit[1] + new_posit[1]) or \
       (current_posit[0] + new_posit[0]) < 0 or \
       (current_posit[1] + new_posit[1]) < 0:
        return False
    return True


for i in range(size):
    current_line = list(input())
    territory.append(current_line)
    if "S" in current_line:
        current_position.append(i)
        current_position.append(current_line.index("S"))

while True:
    command = input()
    new_direction = new_position(command)
    territory[current_position[0]][current_position[1]] = "."
    if not position_is_valid(territory, new_direction, current_position):
        print("Game over!")
        break
    new_direction = [new_direction[0]+current_position[0], new_direction[1]+current_position[1]]
    if territory[new_direction[0]][new_direction[1]] == "B":
        territory[new_direction[0]][new_direction[1]] = "."
        for x in range(size):
            if "B" in territory[x]:
                current_position[0] = x
                current_position[1] = territory[x].index("B")
        territory[current_position[0]][current_position[1]] = "S"
    elif territory[new_direction[0]][new_direction[1]] == "*":
        territory[new_direction[0]][new_direction[1]] = "S"
        current_position = [new_direction[0], new_direction[1]]
        food_eaten += 1
    else:
        territory[new_direction[0]][new_direction[1]] = "S"
        current_position = [new_direction[0], new_direction[1]]
    if food_eaten >= 10:
        print("You won! You fed the snake.")
        break


print(f"Food eaten: {food_eaten}")
for i in range(len(territory)):
    print("".join(territory[i]))
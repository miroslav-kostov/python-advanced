rows, collumns = map(int, input().split(" "))

def init_matrix():
    result = []
    for row in range(rows):
        result.append(input().split())
    return result


def validate(cmd):
    result = True
    if cmd[0] != "swap" or len(cmd) < 5:
        print("Invalid input!")
        result = False
    for i in range(1, len(cmd) - 1):
        if not cmd[i].isnumeric():
            result = False
    return result


the_matrix = init_matrix()

while True:
    command = input()
    if command == "END":
        break
    cmd = command.split(" ")
    valid = validate(cmd)
    if not valid:
        print("Invalid input!")
        continue

    else:
        r1 = int(cmd[1])
        c1 = int(cmd[2])
        r2 = int(cmd[3])
        c2 = int(cmd[4])

    if r1 > len(the_matrix) or r2 > len(the_matrix) or c1 > len(the_matrix[0]) or c2 > len(the_matrix[0]):
        print("Invalid input!")
        continue

    first_temp_value = the_matrix[r1][c1]
    second_temp_value = the_matrix[r2][c2]
    the_matrix[r1][c1] = second_temp_value
    the_matrix[r2][c2] = first_temp_value

    for i in the_matrix:
        print(" ".join(i))




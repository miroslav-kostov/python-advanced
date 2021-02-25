


with open(f"C:\\Users\\John\\Desktop\\a_example", "r") as file:

    pizzas_count, team_of_two, team_of_three, team_of_four = [int(x) for x in (file.readline().split())]
    while True:

        line = file.readline()


        if not line:
            break
        print(line.strip())


print(pizzas_count)
print(team_of_two)
print(team_of_three)
print(team_of_four)
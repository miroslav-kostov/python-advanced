n = int(input())
PUSH = "1"
DELETE = "2"
PRINT_MAX = "3"
PRINT_MIN = "4"
list_numbers = []

for i in range(n):
    initial_command = input().split(" ")
    command = initial_command[0]
    if command == PUSH:
        number = initial_command[1]
        list_numbers.append(int(number))
    elif command == DELETE:
        if list_numbers:
            list_numbers.pop()
    elif command == PRINT_MAX:
        if list_numbers:
            print(max(list_numbers))
    elif command == PRINT_MIN:
        if list_numbers:
            print(min(list_numbers))

list_string = []
while list_numbers:
    current_number = str(list_numbers.pop())
    list_string.append(current_number)

result = ", ".join(list_string)
print(result)


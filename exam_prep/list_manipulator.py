def list_manipulator(the_list, command, position, *args):
    current_list = list(map(int, the_list))
    future_position = int
    if position == "end":
        future_position = -1
    elif position == "beginning":
        future_position = 0
    if command == "add":
        if position == "end":
            for i in args:
                current_list.append(i)
        elif position == "beginning":
            for i in range(len(args)-1, -1, -1):
                current_list.insert(0, args[i])
        return current_list
    elif command == "remove":
        if args:
            for _ in range(args[0]):
                current_list.pop(future_position)
            return current_list
        else:
            current_list.pop(future_position)
            return current_list

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

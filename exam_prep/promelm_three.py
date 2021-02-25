def stock_availability(*args):
    inventory = args[0]
    commands = list(args[1:])
    if commands[0] == "delivery":
        for i in range(1, len(commands)):
            inventory.append(commands[i])
    elif commands[0] == "sell":
        if len(commands) > 1:
            if isinstance(commands[1], int):
                for x in range(commands[1]):
                    inventory.pop(0)
            else:
                for x in range(1, len(commands)): #might be error
                    while commands[x] in inventory:
                        inventory.remove(commands[x])
        else:
            inventory.pop(0)

    return inventory

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

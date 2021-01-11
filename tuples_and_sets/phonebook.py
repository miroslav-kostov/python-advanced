total_searches = 0
phonebook = {}

while True:
    command = input()
    if command.isnumeric():
        total_searches = int(command)
        break
    idx = command.split("-")
    name = idx[0]
    number = idx[1]
    phonebook[name] = number

for i in range(total_searches):
    search = input()
    if search in phonebook:
        print(f"{search} -> {phonebook[search]}")
    else:
        print(f"Contact {search} does not exist.")
def creator(file_name):
    with open(f"{file_name}", "w") as file:
        return


def adder(file_name, content):
    try:
        with open(f"{file_name}", "a") as file:
            file.write(content+"\n")
            return
    except:
        creator(file_name)
        adder(file_name, content)


def replacer(file_name, old_string, new_string):
    try:
        with open(f"{file_name}", "r+") as file:
            text = ''.join(file.readlines())
            replaced_content = text.replace(old_string, new_string)
            file.seek(0)
            file.write(replaced_content)
    except FileNotFoundError:
        print("An error occurred")


def deleter(file_name):
    try:
        os.remove(file_name)
        return
    except FileNotFoundError:
        print("An error occurred")


while True:
    command = input()
    if command == "End":
        break
    current_command = command.split("-")
    idx = current_command[0]
    if idx == "Create":
        name = current_command[1]
        creator(name)
    elif idx == "Add":
        name = current_command[1]
        content = current_command[2]
        adder(name, content)
    elif idx == "Replace":
        replacer(current_command[1], current_command[2], current_command[3])
    elif idx == "Delete":
        deleter(current_command[1])
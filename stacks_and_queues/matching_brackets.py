expression = input()
starts = []
ends = []
for i in range(len(expression)):
    if expression[i] == "(":
        starts.append(i)
    elif expression[i] == ")":
        print(f"{expression[(starts.pop()):i+1]}")

from collections import deque

parenthesis = input()
is_balanced = True
opening = []

mirror = {"{" : "}", "(" : ")", "[" : "]"}

for p in parenthesis:
    if p in "{([":
        opening.append(p)
    else:
        if not opening:
            is_balanced = False
            break
        current_oppening_p = opening.pop()
        if not mirror[current_oppening_p] == p:
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")
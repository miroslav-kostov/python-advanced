def multiply(*args):
    y = 1
    for i in args:
        y *= i
    return y

print(multiply(1, 4, 5))
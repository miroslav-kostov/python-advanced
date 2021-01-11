def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)

# def recursive_power(number, power):
#     return number ** power

print(recursive_power(2, 10))
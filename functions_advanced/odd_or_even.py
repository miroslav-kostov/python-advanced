def even(number):
    if number % 2 == 0:
        return True
    else:
        return False
def odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

command = input()
numbers = list(map(int, input().split()))
if command == "Odd":
    print(f"{sum(filter(odd, numbers)) * len(numbers)}")
elif command == "Even":
    print(f"{sum(filter(even, numbers)) * len(numbers)}")
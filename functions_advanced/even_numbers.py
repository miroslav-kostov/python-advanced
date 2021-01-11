#def remove_odd_numbers(number):
#    if number % 2 == 0:
#        return True
#    else:
#        False

numbers = map(int, input().split())
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)

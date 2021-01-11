n = int(input())
odd_numbers = set()
even_numbers = set()
sum_odds = 0
sum_evens = 0

for x in range(1, n + 1):
    name = input()
    name_value = 0
    for char in name:
        name_value += ord(char)
    name_value = name_value // x
    if name_value % 2 == 0:
        even_numbers.add(name_value)
    else:
        odd_numbers.add(name_value)

for y in odd_numbers:
    sum_odds += y
for z in even_numbers:
    sum_evens += z

if sum_evens == sum_odds:
    result = ", ".join([str(x) for x in odd_numbers.union(even_numbers)])
    print(result)
elif sum_evens < sum_odds:
    result = ", ".join([str(x) for x in odd_numbers.difference(even_numbers)])
    print(result)
elif sum_evens > sum_odds:
    result = ", ".join([str(x) for x in odd_numbers.symmetric_difference(even_numbers)])
    print(result)
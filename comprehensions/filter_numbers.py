start, end = int(input()), int(input())
DIVISORS = {x for x in range(2, 11)}

print([y for y in range(start, end + 1) if any(y % i == 0 for i in DIVISORS)])
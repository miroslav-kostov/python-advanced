n, m = input().split()
n = int(n)
m = int(m)
set_one = set()
set_two = set()


for _ in range(n):
    set_one.add(input())
for _ in range(m):
    set_two.add(input())

set_three = set_one.intersection(set_two)

for i in set_three:
    print(i)
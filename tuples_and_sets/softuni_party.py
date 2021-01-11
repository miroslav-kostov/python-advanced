n = int(input())
guests = set()
arrived = set()

for _ in range(n):
    guests.add(input())

while True:
    command = input()
    if command == "END":
        break
    arrived.add(command)

not_arrived = set(guests).difference(arrived)
vip = set()
not_vip = set()

for guest in not_arrived:
    if guest[0].isnumeric():
        vip.add(guest)
    else:
        not_vip.add(guest)

vip = sorted(vip)
not_vip = sorted(not_vip)

print(len(not_arrived))
for guest in vip:
    print(guest)
for guest in not_vip:
    print(guest)
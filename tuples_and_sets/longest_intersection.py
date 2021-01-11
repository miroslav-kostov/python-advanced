n = int(input())
longest_intersection = 0
intersect_start = 0
intersect_end = 0
intersection_list = []

for _ in range(n):
    current_sequence = input().split("-")
    a, b = current_sequence[0].split(",")
    c, d = current_sequence[1].split(",")
    current_list = sorted([int(a), int(b), int(c), int(d)])
    e, f = current_list[1], current_list[2]
    if f - e > longest_intersection:
        longest_intersection = f - e
        intersect_start = e
        intersect_end = f

for x in range(intersect_start, intersect_end + 1):
    intersection_list.append(x)

print(f"Longest intersection is {intersection_list} with length {len(intersection_list)}")





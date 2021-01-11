n = int(input())
longest_intersection = 0
intersect_start = 0
intersect_end = 0
intersection_list = []

for _ in range(n):
    current_sequence = input().split("-")
    a, b = current_sequence[0].split(",")
    c, d = current_sequence[1].split(",")
    first_seq = range(int(a), int(b) + 1)
    second_seq = range(int(c), int(d) + 1)
    intersection = set(first_seq).intersection(second_seq)
    intersection_list.append(intersection)

longest_one = []
for inter in intersection_list:
    if len(inter) > len(longest_one):
        longest_one = inter

longest_one = list(longest_one)

print(f"Longest intersection is {longest_one} with length {len(longest_one)}")
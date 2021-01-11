categories = {x: [] for x in input().split(", ")}
deliveries = int(input())
quality = 0
quantity = 0

for _ in range(deliveries):
    category, type_item, characteristic = input().split(" - ")
    if category in categories:
        if type_item not in categories[category]:
            categories[category].append(type_item)
    idxes = characteristic.split(";" or ":")
    for idx in idxes:
        index = idx.split(":")
        if index[0] == "quantity":
            quantity += int(index[1])
        elif index[0] == "quality":
            quality += int(index[1])

print(f"Count of items: {quantity}")
print(f"Average quality: {(quality/len(categories)):.2f}")
[print(f"{cat} -> {', '.join(categories[cat])}") for cat in categories]


# data = input()
# data = data.split(" ")
# data = [float(x) for x in data]
# data_dict = {}
# for i in data:
#     if i not in data_dict:
#         data_dict[i] = 1
#     elif i in data_dict:
#         data_dict[i] += 1
#
# for b in data_dict:
#     print(f"{b} - {data_dict[b]} times")

data = tuple(map(float, input().split(" ")))

data_dict = {}
for i in data:
    if i not in data_dict:
        data_dict[i] = 1
    elif i in data_dict:
        data_dict[i] += 1

for b,c in data_dict.items():
    print(f"{b} - {c} times")

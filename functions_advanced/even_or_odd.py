# def even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# def odd(number):
#     if number % 2 != 0:
#         return True
#     else:
#         return False
#
# def even_odd(*args):
#     the_list = []
#     result = []
#     for i in args:
#         if i == "even":
#             result = list(filter(even, the_list))
#         elif i == "odd":
#             result = list(filter(odd, the_list))
#         else:
#             the_list.append(i)
#     return result

def even_odd(*args):
    command = args[-1]
    if command == "even":
        return list(filter(lambda x: x % 2 == 0, args[0: -1]))
    else:
        return list(filter(lambda x: x % 2 != 0, args[0: -1]))

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
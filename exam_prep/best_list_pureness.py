def best_list_pureness(*the_list):
    pureness_value = 0
    count_rotations = 0
    current_best_pureness = 0
    max_rotations = the_list[-1]
    the_actual_list = the_list[0]
    for i in range(max_rotations+1):
        for x in range(len(the_actual_list)):
            current_best_pureness += the_actual_list[x] * x
        if current_best_pureness > pureness_value:
            pureness_value = current_best_pureness
            count_rotations = i
        the_actual_list.insert(0, the_actual_list.pop(-1))
        current_best_pureness = 0
    return f"Best pureness {pureness_value} after {count_rotations} rotations"

test = ([7, 9, 2, 5, 3, 4, 3, 1, 5, 3], 10)
result = best_list_pureness(*test)
print(result)

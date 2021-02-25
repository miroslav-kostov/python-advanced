processes = list(map(int, input().split(", ")))
final_process = int(input())

removed_indexes = []
clock_cycles = 0
current_min_index = int(processes.index(max(processes)))
finished = False

while not finished:
    for i in range(len(processes)):
        for x in range(len(processes)):  # finding the least cycles
            if x not in removed_indexes:
                if processes[x] < processes[current_min_index]:
                    current_min_index = x
        removed_indexes.append(current_min_index)
        clock_cycles += processes[current_min_index]
        if current_min_index == final_process:
            finished = True
            break
        current_min_index = int(processes.index(max(processes)))

print(clock_cycles)

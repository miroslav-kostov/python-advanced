# You are walking in the park and you encounter a snake! You are terrified,
# and you start running zigzag, so the snake starts following you.
# You're tasked to visualize the snake's path in a square form.
# A snake is represented by a string. The isle is a
# rectangular matrix of size NxM. A snake starts going down from the top-left
# corner and slithers its way down. The first cell is filled with the first symbol of the snake,
# the second cell is filled with the second symbol, etc. The snake is
# as long as it takes in order to fill the stairs completely - if you reach the
# end of the string representing the snake,
# start again at the beginning. After you fill the matrix with the snake's path, you should print it.

# Input
#  The input data should be read from the console. It consists of exactly two lines
#  On the first line, you'll receive the dimensions of the stairs in format: N M, where N is the number of
# rows, and M is the number of columns. They'll be separated by a single space
#  On the second line you'll receive the string representing the snake

# Output
#  The output should be printed on the console. It should consist of N lines
#  Each line should contain a string representing the respective row of the matrix

# Constraints
#  The dimensions N and M of the matrix will be integers in the range [1 … 12]
#  The snake will be a string with length in the range [1 … 20] and will not contain any whitespace
# characters

from collections import deque

N, M = map(int, input().split(" "))
data = input()
the_snake = deque(i for i in data)
current_number = 0
isle = []
for row in range(N):
    current_row = []
    for col in range(M):
        current_row.append(current_number)
        current_number += 1
    isle.append(current_row)


for row in range(N):
    if row % 2 == 0:
        for col in range(M):
            current_section = the_snake[0]
            the_snake.append(the_snake.popleft())
            isle[row][col] = current_section
    else:
        for col in range(M - 1, -1, -1):
            current_section = the_snake[0]
            the_snake.append(the_snake.popleft())
            isle[row][col] = current_section

for i in range(N):
    print("".join(isle[i]))
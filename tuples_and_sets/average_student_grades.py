n = int(input())
students_and_grades = {}
for _ in range(n):
    student, grade = tuple(input().split())
    if student not in students_and_grades:
        students_and_grades[student] = [float(grade)]
    else:
        students_and_grades[student].append(float(grade))

for current_student in students_and_grades:
    student_grades = ' '.join(map(lambda grade: f"{grade:.2f}", students_and_grades[current_student]))
    average_grades = f"{sum(students_and_grades[current_student]) / len(students_and_grades[current_student]):.2f}"
    print(f"{current_student} -> {student_grades} (avg: {average_grades})")

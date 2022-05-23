import math
number_of_students = int(input())
number_of_lectures = int(input())
initial_bonus = int(input())

max_bonus = 0
lecture = 0
total_bonus = 0
for student in range(1,number_of_students + 1):
    attendancy = int(input())
    total_bonus = math.ceil(attendancy*(5+initial_bonus)/number_of_lectures)
    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        lecture = attendancy
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {lecture} lectures.")


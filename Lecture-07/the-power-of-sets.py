attendance_week = [
    ["Alice","Bob","Charlie","David"],
    ["Alice","Charlie","David"],
    ["Alice","Bob","David"],
    ["Alice","David","Eve"],
    ["Bob","Charlie","David"]
]

attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)

present_all_days = set.intersection(*attendance_sets)
print("Students present all days:", present_all_days)

all_students = set.union(*attendance_sets)
absent_students = all_students - present_all_days
print("Students absent at least one day:", absent_students)

first_day_present = attendance_sets[0]
last_day_present = attendance_sets[-1]
first_day_but_not_last = list(first_day_present - last_day_present)
print("Students present on the first day but not the last day:", first_day_but_not_last)

unique_students_count = len(all_students)
print("Total unique students:", unique_students_count)
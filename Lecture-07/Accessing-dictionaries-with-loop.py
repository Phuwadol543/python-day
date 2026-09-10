student = {"name": "Alice", "age": 25, "grade": "A", "major": "Computer Science"}

for key in student:
    print(f"{key}: {student[key]}")
    
print()

for key in student.values():
    print(key)
    
print()

for key, value in student.items():
    print(f"{key}: {value}")
student = {'name': 'Alice', 'age': 26, 'major': 'Computer Science'}

print(student.keys())
print(student.values())
print(student.items())

print(student.get('name'))
print(student.get('grade','Not found'))

major = student.pop('major')
print(major)
print(student)

list_item = student.popitem()
print(list_item)
print(student)

student.clear()
print(student)
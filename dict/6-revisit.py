student = {
    'id': 123,
    'grade': 'B',
}
print(student.get("name", "doesn't exist."))
print(student.get("grade", "doesn't exist."))

# model answer: use 'in'
print('name' in student)      # False
print('grade' in student)     # True

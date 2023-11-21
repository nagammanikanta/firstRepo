students_info = {
    'name': 'manikanta',
    'age' : '29',
    'role' :'devops'
}
print(students_info['name'])

del students_info['age']

if 'age' in students_info:
    print('Age is present in the dictionary is 29')

for key, value in students_info.items():
    print(key, value)



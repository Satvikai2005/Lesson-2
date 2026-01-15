student_data = {
    'id1':{"Name":"Riyan", "Age":13, "Class":7},
    'id2':{"Name":"Noone", "Age":14, "Class":8},
    'id3':{"Name":"Riyan", "Age":13, "Class":7},
    'id4':{"Name":"Unknown", "Age":67, "Class":89},
    'id1':{"Name":"Mr.Noob", "Age":10, "Class":10}
}

result = {}

for key, value in student_data.items():
    if key not in result:
        result[key] = value

print(result)
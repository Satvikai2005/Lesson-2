print("Enter marks of 3 subjects:")
s1 = int(input("Subject 1:"))
s2 = int(input("Subject 2:"))
s3 = int(input("Subject 3:"))
total = s1 + s2 + s3
average = total/3
if average>90:
    grade = 'A'
elif average>80:
    grade = 'B'
elif average>70:
    grade = 'C'
elif average>60:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is {grade}")
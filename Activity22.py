a=input("Was it a miracle cause?(Y/N):")
if a == "Y":
    print("You can attend the exam.")
else:
    if a=="N":
        attendance = int(input("Enter your attendance percentage: "))
        if attendance>75:
            print("You can attend the exams.")
        else:
            print("You can not attend the exams. Enjoy!")
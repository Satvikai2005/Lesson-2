#checking the frequency of a value in a dictionary
#asking the user to choose a value to find the values frequency
test_dictonary = {'Codingal' : 2,'is' : 2,'for' : 2,'Coding' : 1}
value = int(input("Choose a value between (1/2) to check the values frequency:"))
if value == 1:
    frequency = 0
    for i in test_dictonary:
        if test_dictonary[i] == 1:
            frequency += 1
    print("The frequency of the value 1 is:",frequency)
elif value == 2:
    frequency = 0
    for i in test_dictonary:
        if test_dictonary[i] == 2:
            frequency += 1
    print("The frequency of the value 2 is:",frequency)
else:
    print("Please choose a valid value next time.")

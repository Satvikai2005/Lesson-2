#accepting the number of rows
x = int(input("Enter the number of rows you want: "))
count = 1
"""
typing the program
typing the outer loop
"""
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(count ,end=" ")
        count += 1
    print()

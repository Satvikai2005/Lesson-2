rows = int(input("Enter the number of rows you want: "))
space = (rows)*2
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*" ,end="")
    #print(space,end="")
    space = space-2 
    #print(space,end="")
    for l in range(space+1):
        print(" ", end="") 
    for k in range(1, i + 1):
        print("*" ,end="")
    print() 
    
    

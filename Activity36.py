#Program to print star
rows=int(input("Enter number of rows: "))
if rows%2==0:
    halfrow=rows//2
else:
    halfrow=rows//2+1
space=halfrow-1
for i in range(1,halfrow+1):
    for j in range(1,space+1):
        print(" ",end="")
    space-=1
    num=1
    for j in range(2*i-1):
        print(num,end="")
        num+=1
    print()
    num=1
if rows%2==0:
    for j in range(2*i-1):
        print(num,end="")
        num+=1
    print()
space=1
for i in range(1,halfrow):
    for j in range(1,space+1):
        print(" ",end="")
    space+=1
    num=1
    for j in range(1,2*(halfrow-i)):
        print(num,end="")
        num+=1
    print()
















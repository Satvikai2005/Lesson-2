x = int(input("Enter a 3 digit number here"))
result = 0
temp = x
while temp>0:
    digit = temp%10
    sum+=digit**3
    temp//10
if x==sum:
    print(f"{x} is an Armstrong number.")
else:
    print(f"{x} is not an Armstrong number.")





CP = int(input("Please enter the cost price: "))
SP = int(input("Please enter the selling price: "))
if SP>CP:
    profit = SP - CP
    print("Congrats! It's a profit of:$ ",profit)
else:
    Loss = CP - SP
    print("Sorry, it's a loss of:$ ",Loss)    
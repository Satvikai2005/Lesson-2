units_consumed = (input("Enter the number of electricity units counsumed: "))
if units_consumed <=50:
    bill_amount = units_consumed *2.60
    tax = 25
elif units_consumed >50 and units_consumed <= 100:
    bill_amount = 130 + (units_consumed - 50) * 3.25
    tax = 35
elif units_consumed >100 and units_consumed <=200:
    bill_amount = 130 + 162.5 + (units_consumed - 100) * 5.26
    tax = 45
else:
    bill_amount = 130 + 162.5 +526 + (units_consumed - 200) * 8.45
    tax = 75
total_bill=bill_amount + tax
print(f"Total electricity bill amount is {total_bill:.2f}")
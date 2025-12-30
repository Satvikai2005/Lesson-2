try:
    x = int(input("Enter the numerator: "))
    y = int(input("Enter the denominator: "))
except ZeroDivisionError as zero:
    print("Denominator cannot be zero.")
except ValueError as v:
    print("An integer is excepted.")
except Exception as e:
    print(e)
else:
    print("Division worked.")
finally:
    print("This line of code will execute no matter what.")















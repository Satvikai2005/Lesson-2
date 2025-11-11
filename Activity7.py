amount = int(input("Enter an amount: "))
notes_100 = amount//100
notes_50 = (amount%100)//50
notes_10 = ((amount%100)%50)//10
print("Notes of 100 needed ", notes_100)
print("Notes of 50 needed ", notes_50)
print("Notes of 10 needed ", notes_10)

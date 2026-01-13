#multiplying the vaue of the tuple by the number user gave
users_number = int(input("Enter a number here to be multiplied: "))
tuple = (1, 3, 5, 7, 9, 11)
i = 0
while i < len(tuple):
    result = tuple[i] * users_number
    print(f"{tuple[i]} x {users_number} = {result}")
    i += 1





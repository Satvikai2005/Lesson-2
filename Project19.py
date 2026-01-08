start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))
melist_even = []
melist_odd = []
for j in range(start_range, end_range + 1):
    print(j**2)
print("Above was the list of squares.")

for i in range(start_range, end_range + 1):
    if i % 2 == 0:
        list.extend(melist_even, [i])
        print(melist_even,end="\n")
        if i % 3 == 0:
            continue
print("Above was a list of even numbers.")

for i in range(start_range, end_range + 1):
    if i % 3 == 0:
        list.extend(melist_odd, [i])
        print(melist_odd,end="\n")
        if i % 2 == 0:
            continue
print("Above was a list of odd numbers.")





def calculate_if_first_andlast_letter_are_same(melist):
    count = 0    
    for x in melist:
        if len(x) >=2 and x[0] == x[-1]:
            count += 1
            print(x)
    return count

melist = ["abcd", "xxx", "R.I.P", "rest in peace", "dad", "hellowh"]
print(calculate_if_first_andlast_letter_are_same(melist))


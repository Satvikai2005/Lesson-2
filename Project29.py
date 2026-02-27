def int_to_roman(num: int) -> str:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

if __name__ == "__main__":
    try:
        user_input = input("Enter a number to convert to Roman numeral: ")
        number = int(user_input)
        if number <= 0:
            print("Please enter a positive integer.")
        elif number >= 4000:
            print("Roman numerals typically support numbers up to 3999.")
        else:
            print(f"Roman numeral: {int_to_roman(number)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
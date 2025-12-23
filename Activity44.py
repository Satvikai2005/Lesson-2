def cube(number):
    return number * number * number
def is_divisible_by_3(number):
    if number % 3 == 0:
        return f"Cube of {number} is {cube(number)}."
    else:
        return f"{number} is not divisible by 3."
print(is_divisible_by_3(9))
print(is_divisible_by_3(10))















tuple = (1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1)
sunny = 0
rainy = 0
for weather in tuple:
    if tuple[weather] == 0:
        sunny += 1
    else:
        rainy += 1
if sunny > rainy:
    print("The weather is mostly sunny.")
else:
    print("The weather is mostly rainy.")
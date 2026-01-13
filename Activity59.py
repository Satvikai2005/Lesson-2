tuple = (1, 2, 3, 3, 2, 1)
def flip_flop_tuple(tuple):
    start = 0
    end = 0
    while start < end:
        if tuple[start] != tuple[end]:
            return False
        start += 1
        end -= 1
    return True
riwebviwsvb = flip_flop_tuple(tuple)

if riwebviwsvb:
    print(f"{tuple} is a flip flop tuple: {riwebviwsvb}")
else:
    print(f"{tuple} is not a flip flop tuple: {riwebviwsvb}")
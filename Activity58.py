tuple = (1, "fjvn", 5.0)
new_tuple = tuple + (6, 7, 1, 11)
print(tuple)
print(new_tuple)
print(f"1 occured {new_tuple.count(1)} times in the tuple.")
#slicing
print(new_tuple[5:8])
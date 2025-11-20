mean1 = 48
total_number = 1540
misread_value = 875
correct_value = 67
new_total = mean1*total_number
correctedtotal = new_total - misread_value + correct_value
correct_mean = int(correctedtotal / total_number)
print("The corrected mean is: ",correct_mean)

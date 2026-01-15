toys_basket = {'Guns':4567,'Spaceships':4567,'Marvel':678941,'NOOb SAIBOT toys':9999999999999999}

quantity = 4567
count = 0

for i in toys_basket:
    if toys_basket[i] == quantity:
        count += 1

print(f"There are {count} toys with the quantity {quantity}.")
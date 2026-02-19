class Computer:
    _max_price = 100

    def sell(self):
        print(f"The maximum selling price is {Computer._max_price}")

    def set_maxprice(self, max_price):
        Computer._max_price = max_price
o = Computer()
o._max_price = 1000
o.sell()
o.set_maxprice(1500)
o.sell()
class Shoes:
    def __init__(self, brand, color, price):
        self.__brand = brand
        self.__color = color
        self.__price = price

    def perks(self):
        print("comfortable fit")
# created class with multiple private attributes

        retailer = Shoes("nike", "black and white")
        print(retailer.__brand)
        print(retailer.__color)

class Sunglasses:
    def __init__(self, make, style):
        self._make = make
        self._style = style

        store = Sunglasses("Versace", "classy")
        print(store._make)
        print(store._style)






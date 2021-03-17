class Pub:

    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks


    def find_drink(self, drink_item):
        for drink in self.drinks:
            if drink == drink_item:
                return drink

    def sell_drink(self, drink):
        self.till += drink.price
    
 



# drinks = ["Magner's", "Gin Sour", "EFES", "Sourz"]



# for drink in drinks:
#     if drink == "EFES":
#         print("ok")

# def find_drink(drink_name):
#     for drink in drinks:
#         if drink == drink_name:
#             return drink_name

# test = find_drink("EFES")
# print(test)

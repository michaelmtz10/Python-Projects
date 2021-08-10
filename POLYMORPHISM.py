class manufacture:
    name = "Toyota Corolla"
    year = 2021
    price = 32000

    def vehicleInfo(self):
        model_name = input("Enter the model: ")
        model_year = input("Enter the date: ")
        model_price = input("Enter the price: ")
        if (model_year == self.year and model_price == self.price):
            print("The model for this make is {}".format(model_name))
        else:
            print("This is not apart of the manufactures manifest!")

class warehouse(manufacture):
    part_name = "Alternator"
    part_color = "Black"
    part_specialist = "Engine Doc"


class dealership(manufacture):
    brand = "Toyota"
    location = "Seattle"
    Price = 0







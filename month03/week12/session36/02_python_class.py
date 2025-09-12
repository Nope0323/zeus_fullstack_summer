class Car():
    # TODO
    # Классыг ашиглах
    def __init__(self, brand, model ):
        self.brand = brand
        self.model = model
    def show_info(self):
        print(f"Машины марк: {self.brand}, Загвар: {self.model}")


my_car = Car("Toyota", "Prius")
my_car1 = Car("Mercedes","Benz")



my_car.show_info()
my_car1.show_info()
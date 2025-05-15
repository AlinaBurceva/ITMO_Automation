class Car:
    def __init__(self, color, type, year ):
        self.color  = color
        self.type  = type
        self.year  = year

    def start_car(self):
        print('Автомобиль заведен')

    def turn_off_car(self):
        print('Автомобиль заглушен')

    def year_car(self):
        return self.year

    def type_car(self):
        return self.type

    def color_car(self):
        return self.color

car_1 = Car('red', 'sidan', 2024)

car_1.start_car()
car_1.turn_off_car()
print(car_1.year_car())
print(car_1.type_car())
print(car_1.color_car())








from contextlib import nullcontext


class Soda:
    def __init__(self, dob=None):
        self.dob = dob

    def show_my_drink(self):
        if self.dob:
            print('Газировка и ' + self.dob)
        else:
            print('Обычная газировка')


soda = Soda('Дюшес')
soda_2 = Soda()

soda.show_my_drink()
soda_2.show_my_drink()

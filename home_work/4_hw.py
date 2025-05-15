#создайте класс прямоугольника.
class Rectangle:
    def __init__(self, width = None, height = None):
        self.width = width
        self.height = height

    def square(self):
        print(f'S={self.width * self.height}')

    def perimeter(self):
        print(f'P={(self.width + self.height) * 2}')

Obj_1 = Rectangle(5, 6)
Obj_2 = Rectangle(7, 7)
Obj_3 = Rectangle(15, 6)

Obj_1.perimeter()
Obj_1.square()
Obj_2.perimeter()
Obj_2.square()
Obj_3.perimeter()
Obj_3.square()

#Создайте класс Math.
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
class Math:
    def __init__(self, a = None, b = None):
        self.a = a
        self.b = b

    def addition(self):
        print(f'addition={self.a + self.b}')
    def multiplication(self):
        print(f'multiplication={self.a * self.b}')
    def division(self):
        print(f'division={self.a / self.b}')
    def subtraction(self):
        print(f'subtraction={self.a - self.b}')

Obj = Math(15, 5)


Obj.addition()
Obj.multiplication()
Obj.division()
Obj.subtraction()

#https://demoqa.com/text-box
class Sidebar():
    def __init__(self, text, typ, loc = None):
        self.text = text
        self.typ = typ
        self.loc = loc

    def click_btn(self):
        print(f"Клик по кнопке {self.text}")

sidebar_TextBox = Sidebar('Text Box', 'button')
sidebar_Check_Box = Sidebar('Check Box', 'button')
sidebar_Radio_Button = Sidebar('Radio Button', 'button')

print(sidebar_TextBox.text)
sidebar_TextBox.click_btn()
print(sidebar_Check_Box.text)
sidebar_Check_Box.click_btn()
print(sidebar_Radio_Button.text)
sidebar_Radio_Button.click_btn()










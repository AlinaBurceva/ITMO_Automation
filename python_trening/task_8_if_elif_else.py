num_float = 3.4

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

permit_print = True
num = 2

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def student_year(kurs):
    if kurs in (1, 2, 3, 4):
        print('Бакалавр')
    elif kurs in (5, 6):
        print('Магистр')
    elif kurs in (7, 8, 9):
       print('Аспирант')
    else:
        print('Введите корректный год обучения')

student_year(5)

def calc(num):
    if num > 100 or num < -100:
        print('-')
    else:
        print('+')


calc(105)
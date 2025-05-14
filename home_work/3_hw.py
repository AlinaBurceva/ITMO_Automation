#Функция на вход получает два произвольных числа.
#Вывести в консоль наибольшее из чисел.
def if_num(num_1, num_2):
    if num_1 > num_2:
        print(num_1)
    else:
        print(num_2)

if_num(15, 10)

#Функция на вход получает два произвольных числа.
# Вывести в консоль “yes”, если они отличаются друг от друга на 135,
# иначе вывести на экран “No”
def if_bool(num_1, num_2):
    if (abs(num_1 - num_2) == 135) or (abs(num_2 - num_1) == 135):
        print('Yes')
    else:
        print('No')

if_bool(5, -130)

#Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль (зима, весна, лето, осень)
def month_season(num_m):
    if num_m in (12, 1, 2):
        print('Зима')
    elif num_m in (3, 4, 5):
        print ('Весна')
    elif num_m in (6, 7, 8):
        print('Лето')
    elif num_m in (9, 10, 11):
        print('Осень')
    else:
        print('Введите корректный номер месяца')

month_season(11)

#Функция на вход получает три произвольных числа.
# Если все числа больше 10, то вывести на экран “yes”, иначе “no”;
def nums_3(num_1, num_2, num_3):
    if (num_1 > 10) and (num_2 > 10) and (num_3 > 10):
        print("Yes")
    else:
        print('No')

nums_3(1, 13, 14)

#Функция на вход получает список, состоящий из 5 произвольных чисел.
#Найти количество положительных чисел среди них.
def list_cnt(num_1, num_2, num_3, num_4, num_5):
    list_c = [num_1, num_2, num_3, num_4, num_5]
    cnt_num = 0
    for lists in list_c:
        if lists > 0:
            cnt_num = cnt_num + 1

    print(cnt_num)


list_cnt( 1,-5,3,4,0)

#Функция на вход получает 2 переменные.
#a. Кол-во лет (int)
#b. Кол-во месяцев (int)
#Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
def day_cnt(year_cnt: int, month_cnt: int):
    if year_cnt >= 0 and month_cnt >= 0:
        print((year_cnt * 12 * 29) + (month_cnt * 29))
    else:
        if year_cnt < 0:
            print('Кол-во лет должно быть >= 0')
        if  month_cnt < 0:
            print('Кол-во месяцев должно быть >= 1')


day_cnt(1,0)







def task_1():
    a: int = 5
    b: float = 1.3
    c: str = 'строка'
    d: list = [1, 2]
    e: bool = True

    print('Тип a: ', type(a))
    print('Тип b: ', type(b))
    print('Тип c: ', type(c))
    print('Тип d: ', type(d))
    print('Тип e: ', type(e))

task_1()

def task_2():
    a: list =  [1, 2, 3, 5, 8, 13, 21]

    return(a[0:3])

print(task_2())


def task_3(a: int = 3):
    return a ** 2

print(task_3())






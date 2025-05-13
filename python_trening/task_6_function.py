def add(x, y):
    return x + y

print(add(1, 2))

print(add('I am ', 'tester'))

def arg(a, b, c = 2, d = 3):
    return a + b + c + d

print(arg(1, 1, 1, 1))

print(arg(2, 2))

print(arg(1, 1, 1))

print(arg(2, 2, 0.3, 1))

def arg_range(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(arg_range('1','2','3','4'))

print(arg_range('1','2', d='3', c='4'))


def f1(a = (1, 2, 3, 4)):
    return a[1]
print(f1())


def f2(radius,pi=3.14159):
    return pi * radius ** 2
print(f2(3))
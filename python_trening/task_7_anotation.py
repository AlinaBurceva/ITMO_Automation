a: int = 5
b: str = 'строка'
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print(indent('123', 123))

def l1(s: str) -> int:
    return len(s)
print(l1('test'))

def l2(s1: str, s2: str) -> int:
    return max(len(s1), len(s2))
print(l2('test', 'testing'))

def list1(l : list = [1, 2, 3]) -> list:
    l.append(4)
    return l
print(list1())

def list2(l : list = [1, 2, 3]) -> int:
    return sum(l)
print(list2())







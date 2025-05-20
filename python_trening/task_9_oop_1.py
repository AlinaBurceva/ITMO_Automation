#
# class Input:
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
#
#
# # print(search.loc)
#
# class Button:
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
# class Title:
#     def __init__(self, text,loc):
#         self.loc = loc
#         self.text = text
#
# class Link:
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
# search = Input('input','input#search')
# button = Button('button', 'loc#button')
# title = Title('title', 'loc#title')
# link = Link('link', 'loc#link')
#
# print('Кнопка ' + search.text + ' имеет loc ' + button.loc)
# print('Кнопка ' + button.text + ' имеет loc ' + button.loc)
# print('Кнопка ' + title.text + ' имеет loc ' + button.loc)
# print('Кнопка ' + link.text + ' имеет loc ' + button.loc)

#ДЗ
from task_9_checks import Checks


class Input(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc



# print(search.loc)

class Button(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

class Title(Checks):
    def __init__(self, text,loc):
        self.loc = loc
        self.text = text

class Link(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search = Input('input','input#search')
button = Button('button', 'loc#button')
title = Title('title', 'loc#title')
link = Link('link', 'loc#link')

print(search.check_text())
print(button.check_text())
print(title.check_text())
print(link.check_text())











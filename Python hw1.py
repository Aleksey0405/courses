# Python. HW_1

# 1) Создать переменную типа String
# 2) Создать переменную типа Integer
# 3) Создать переменную типа Float
# 4) Создать переменную типа Bytes
# 5) Создать переменную типа List
# 6) Создать переменную типа Tuple
# 7) Создать переменную типа Set
# 8. Создать переменную типа Frozen set
# 9) Создать переменную типа Dict
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
# 17) (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.
# Выгрузить файл в Git репозиторий.



#Tasks1-10
from pickle import FROZENSET


String = 'Привет'
print(String,"Type:",type(String))
Integer = 10
print(Integer,"Type:",type(Integer))
Float = 0.5
print(Float,"Type:",type(Float))
Bytes = bytes(10)
print(Bytes,"Type:",type(Bytes))
List = [1,2,3,4]
print(List,"Type:",type(List))
Tuple = (1,3,5,7)
print(Tuple,"Type:",type(Tuple))
Set = {'car'}
print(Set,"Type:",type(Set))
FrozenSet = frozenset(Set)
print(FrozenSet,"Type:",type(FrozenSet))
My_dict = {'name':'Alex', 'age':'24'}
print(My_dict,"Type:",type(My_dict))


#Task11
a="Я хочу стать"
b="QA."
c = a+" "+b
print(c)

#Task12
a = 5
b = 7
plus = a+b
print(plus)

#Task13
division = a/b
print(division)

#Task14
multiply = (a*b)
print(multiply)

#Task15
division = a//b
print(division)

#Task16
rest = a%b
print(rest)

#Task17
print((7+12) ** 3 + 7 * 4 - 44 / 2 ** 4)

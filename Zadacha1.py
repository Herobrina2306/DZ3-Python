# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3, 4, 5, 6, 7, 8, 9, 1, 11]


def sum(lst_):
    b = 0
    for i in range(1, len(lst_), 2):
        b += lst_[i]    
    return b


print(lst, ' -> ', sum(lst))
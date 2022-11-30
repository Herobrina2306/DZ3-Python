# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst1 = [2, 3, 4, 5, 6]
lst2 = [2, 3, 5, 6]


def proezved(lst_):
    lst_f = []
    for i in range(int(len(lst_) / 2)):
        n = lst_[i] * lst_[-i - 1]
        lst_f.append(n)
    if len(lst_) % 2 == 1:
        l = lst_[int(len(lst_) / 2)] ** 2
        lst_f.append(l)
    return lst_f


print(lst1, ' -> ', proezved(lst1))
print(lst2, ' -> ', proezved(lst2))
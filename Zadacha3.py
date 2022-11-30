# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


lst = [1.1, 1.2, 3.1, 5, 10.01]
lst1 = []

for i in range(len(lst)):
    n = round(lst[i] % 1, 5)
    lst1.append(n)
    if n == 0:
        lst1.remove(0)
    

print(lst1)


def ost(lst_):
    min = float('inf')
    max = float('-inf')
    for i in range(len(lst_)):
        m = lst_[i]
        if min > m:
            min = m
        if max < m:
            max = m
        fin = max - min
    return fin


print(ost(lst1))
        

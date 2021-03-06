﻿# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм
# (сделайте его умнее).


import random
import timeit

source_array = []
length = random.randint(10,20)
for i in range(length):
    source_array.append(random.randint(-100, 100))
print(source_array)
array = source_array
arrray = source_array

def bubble_sorting():
    for i in range(len(array), 0, -1):
        for j in range(1, i):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
                # print(array)
    # return array
    # print(array)

def shaker_sorting():
    min = 0
    max = len(arrray) - 1
    while min <= max:
        for i in range(min, max, +1):
            if arrray[i] > arrray[i + 1]:
                arrray[i], arrray[i + 1] = arrray[i + 1], arrray[i]
                # print(arrray)
        max -= 1

        for j in range(max, min, -1):
            if arrray[j - 1] > arrray[j]:
                arrray[j], arrray[j - 1] = arrray[j - 1], arrray[j]
                # print(arrray)
        min += 1
    # return arrray
    # print(arrray)

# a = bubble_sorting(source_array)
# b = shaker_sorting(source_array)

print(timeit.timeit("bubble_sorting()", setup="from __main__ import bubble_sorting", number=1000))
print(timeit.timeit("shaker_sorting()", setup="from __main__ import shaker_sorting", number=1000))

print(array)
print(arrray)

# применено улучшение пузырьковой сортировки - шейкерная сортировка. происходит дополнительная 
# сортировка при повсторном проходе во встречном направлении. Измерение быстродействия показывает,
# что некоторое улучшения есть, как правило шейкерная сортировка быстрее, иногда даже в несколько раз.
# По-видимому это зависит от структуры исходного массива. 

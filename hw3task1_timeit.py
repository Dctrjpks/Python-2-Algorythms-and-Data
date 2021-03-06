# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
# из чисел в диапазоне от 2 до 9.
import sys
import collections
from pympler import asizeof
import timeit

def fixed_range_double_cycle():
    div = [0,0,0,0,0,0,0,0]
    print('В диапазоне  2 ... 99')
    for i in range(2,10):
        for j in range(2,100):
            if j%i==0:
                div[i-2] += 1
        print('на ', i, ' делится ', div[i-2], 'чисел')

def fixed_range_empiric():
    div = [0]*8
    # print('В диапазоне  2 ... 99')
    for i in range(2,10):
        div[i-2]=99//i
        print('на ', i, ' делится ', div[i-2], 'чисел')

def universal_double_cycle():
    a = 2
    b = 99
    c = 2
    d = 9
    div = [0] * (d - c + 1)
    print('В диапазоне ', a, '... ', b)
    for i in range(c, d + 1):
        for j in range(a, b + 1):
            if j % i == 0:
                div[i - 2] += 1
        print('на ', i, ' делится ', div[i - 2], 'чисел')

def universal_empiric():
    a = 2
    b = 99
    c = 2
    d = 9
    div=[0]*(d-c+1)
    print('В диапазоне ', a, '... ', b)
    for i in range(c,d+1):
        div[i-2] = b // i - a//i
        print('на ', i, ' делится ', div[i - 2], 'чисел')

fixed_range_double_cycle()
fixed_range_empiric()
universal_double_cycle()
universal_empiric()

# print(10*timeit.timeit("fixed_range_double_cycle()", setup="from __main__ import fixed_range_double_cycle", number=100000))
# print(10*timeit.timeit("fixed_range_empiric()", setup="from __main__ import fixed_range_empiric", number=100000))
# print(10*timeit.timeit("universal_double_cycle()", setup="from __main__ import universal_double_cycle", number=100000))
# print(10*timeit.timeit("universal_empiric()", setup="from __main__ import universal_empiric", number=100000))

# TimeIt :
# 128.079792599965
# 2.0912308998958906
# 122.06772060017101
# 2.7089843999419827
# #
print('fixed_range_double_cycle')
print(asizeof.asizeof(2))
print(asizeof.asizeof(9))
print(asizeof.asizeof(2))
print(asizeof.asizeof(99))
print(asizeof.asizeof(div))
print(asizeof.asizeof(i))
print(asizeof.asizeof(j))

print('fixed_range_empiric')
print(asizeof.asizeof(2))
print(asizeof.asizeof(9))
print(asizeof.asizeof(2))
print(asizeof.asizeof(99))
print(asizeof.asizeof(div))
print(asizeof.asizeof(i))

print('universal_double_cycle')
print(asizeof.asizeof(a))
print(asizeof.asizeof(b))
print(asizeof.asizeof(c))
print(asizeof.asizeof(d))
print(asizeof.asizeof(i))
print(asizeof.asizeof(j))
print(asizeof.asizeof(div))

print('universal_empiric')
print(asizeof.asizeof(a))
print(asizeof.asizeof(b))
print(asizeof.asizeof(c))
print(asizeof.asizeof(d))
print(asizeof.asizeof(i))
print(asizeof.asizeof(div))


# не заработал анализ памяти. Ни из IDE, ни через консоль.
# не найден модуль pympler
# версия Пайтона - 3.7.3, разрядность - 32 бита.
#
# По производительности алгоритмы, основанные на эмпирических
# соответсвиях действительно примерно в 50 раз более производительны.
# По памяти более экономичным из них должен быть 2-й, fixed_range_empiric.
# 4-ый, universal_empiric, при более низкой производительности
# скорее всего ещё и несколько проигрывает по потреблению памяти, но
# универсален, и может применяться для любых диапазонов целых чисел.
#
# Причём алгоритм 3, основанный на переборе данных будет ещё более замедляться
# при расширении диапазонов, да ещё и в зависимости близкой к квадратичной.
# Универсальный эмпирический алгоритм всегда будет в 2 (по TimeIt - в 1,35) раза
# медленнее фиксированного, т.к. выполняет двойную работу. Сначала по формуле
# определяет все кратные от 1 до верхней границы диапазона, потом из этого
# вычитает кратные до нижней границы.
#
# Если не требуется универсальность - то выбор безусловно - № 2.
# За возможность обрабатывать любые числа алгоритмом № 4 надо заплатить
# снижением производительности раза в 1.35. Потребление памяти не должно быть
# критичным ни в одном из вариантов.
#

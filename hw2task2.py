# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).

odd_figures = '13579'
even_figures = '02468'
odd = 0
even = 0
number = input('Введите натуральное число: ')
# print (number, len(number))
i = 0
for i in range(len(number)):
    if number[i] in odd_figures:
        odd += 1
    else:
        even += 1
print ('В числе', number, 'чётных', even, 'нечётных', odd)


# 8. Определить, является ли год, который ввел пользователем, високосным
# или невисокосным.

year_num = int(input('Введите год: '))
oo = year_num % 400
if oo == 0:
    print ('Год', year_num, 'високосный.')
else:
    ooo = year_num % 100
    if ooo == 0:
        print ('Год', year_num, 'невисокосный.')
    else:
        o = year_num % 4
        if o == 0:
            print ('Год', year_num, 'високосный.')
        else:
            print ('Год', year_num, 'невисокосный.')
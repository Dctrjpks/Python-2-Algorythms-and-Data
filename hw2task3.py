# 3. Сформировать из введенного числа обратное по порядку входящих
# в него цифр и вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.

dirnum = input('введите натуральное число: ')
backnum = ''

i=0
for i in range(len(dirnum)):
    backnum = backnum + dirnum[len(dirnum)-i-1]
print(dirnum)
print(backnum)

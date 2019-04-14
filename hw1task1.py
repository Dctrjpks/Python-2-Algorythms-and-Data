# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.
num = []
while len(num) != 3:
    num = input('Введите трёхзначное число: ')
summ = int(num[0]) + int(num[1]) + int(num[2])
prod = int(num[0]) * int(num[1]) * int(num[2])
print('Сумма цифр числа:', summ)
print('Произведение цифр числа:', prod)

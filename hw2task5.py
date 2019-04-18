# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа
# под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
import string
a = 10
for j in range(32, 128, a):
    for i in range(a):
        if i+j > 127:
            break
        print(i+j, chr(i+j), ' | ',end = '')
    print('')
# for i in string.ascii_letters:
#     print(i)
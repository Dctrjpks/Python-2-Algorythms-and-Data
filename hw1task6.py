# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string
# letters_nums = []
eng_alph = 'abcdefghijklmnopqrstuvwxyz'
rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
let_num = int(input('Введите номер буквы :'))
# print(let_num+1)
# print(eng_alph[let_num-1])
if let_num-1 > len(rus_alph):
    print('Такой буквы нет ни в русском, ни в английском алфавите')
elif let_num - 1 > len(eng_alph):
    print('Такой буквы нет в английском алфавите')
    print('Буква с номером "{}" в русском алфавите - {}.'.format(let_num, rus_alph[let_num - 1]))
else:
    print('Буква с номером "{}" в английском алфавите - {}.'.format(let_num, eng_alph[let_num-1]))
    print('Буква с номером "{}" в русском алфавите - {}.'.format(let_num, rus_alph[let_num-1]))

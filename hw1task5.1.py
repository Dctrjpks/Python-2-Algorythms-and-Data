# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита
# они стоят  и сколько между ними находится букв.
import string
eng_alph = 'abcdefghijklmnopqrstuvwxyz'
rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
let_inp_1 = '0'
while let_inp_1.lower() not in eng_alph and let_inp_1.lower() not in rus_alph:
    let_inp_1 = input('Введите первую букву :')
let_inp_2 = '0'
if let_inp_1.lower() in eng_alph:
    while let_inp_2.lower() not in eng_alph:
        let_inp_2 = input('Введите вторую букву того же алфавита:')
    let1 = let_inp_1.lower()
    let2 = let_inp_2.lower()
    let_place_1 = eng_alph.find(let1) + 1
    let_place_2 = eng_alph.find(let2) + 1
    print('Номер буквы "{}" в английском алфавите - {}.'.format(let1, let_place_1))
    print('Номер буквы "{}" в английском алфавите - {}.'.format(let2, let_place_2))
    print('Между ними {} букв.'.format(abs(let_place_2 - let_place_1) - 1))
else:
    while let_inp_2.lower() not in rus_alph:
        let_inp_2 = input('Введите вторую букву того же алфавита:')
    let1 = let_inp_1.lower()
    let2 = let_inp_2.lower()
    let_place_1 = rus_alph.find(let1)+1
    let_place_2 = rus_alph.find(let2)+1
    print('Номер буквы "{}" в русском алфавите - {}.'.format(let1, let_place_1))
    print('Номер буквы "{}" в русском алфавите - {}.'.format(let2, let_place_2))
    print('Между ними {} букв.'.format(abs(let_place_2 - let_place_1) - 1))
print ('У этого способа есть потенциал для перевода на ООП')

# ИГРА В КОСТИ. PVP ИЛИ PVE

#выбор - игра с человеком или с компьютером
#ввести имя
#рандом числа
#условия победы
#прописать исключения
#ответ выделить цветом
#создать цикл

import time
import random as r
from colorama import Fore, Back, Style

print ('Игра - Кости\n')
time.sleep (1)

while True:
    qw = input ("""Выберите тип игры:
1. С человеком
2. С компьютером
""")
    if qw == "1":
        time.sleep (1)
        print ('\nДобро пожаловать в игру!\n')
        name_1 = input ('Имя первого игрока: ')
        name_2 = input ('Имя второго игрока: ')
        
        time.sleep (1)
        print (input ('\n' + name_1 + ', для броска нажмите - Enter: '))
        time.sleep (1)
        br_1 = r.randint (1, 6) 
        print ('Результат: ' + Fore.RED + str(br_1) + Style.RESET_ALL)
        
        
        time.sleep (1.5)
        print (input ('\n' + name_2 + ', для броска нажмите - Enter: '))
        time.sleep (1)
        br_2 = r.randint (1, 6)
        print ('Результат: ' + Fore.RED + str(br_2) + Style.RESET_ALL)
        
        time.sleep (1.5)
        if br_1 > br_2:
            print ('\n' + Fore.RED + name_1 + ' - Победитель.' + Style.RESET_ALL)
            time.sleep (1)
            print ('\nПоздравляю, ' + name_1 + ''', но зазнаваться не стоит. Сегодня - вы, завтра кто-то другой.''')
        elif br_1 == br_2:
            print ('\n' + Fore.RED + 'У вас - Ничья!' + Style.RESET_ALL)
        else:
            print ('\n' + Fore.RED + name_2 + ' - Победитель.' + Style.RESET_ALL)
            time.sleep (1)
            print ('\nПоздравляю, ' + name_2 + ''', но зазнаваться не стоит. Сегодня - вы, завтра кто-то другой.''')
        
    elif qw == '2':
        time.sleep (1)
        print ('\nДобро пожаловать в игру!\n')
        name_1 = input ('Напишите ваше имя: ')
        name_2 = ('Компьютер')
        print ('Второй игрок: ' + name_2)
        
        time.sleep (1)
        print (input ('\n' + name_1 + ', для броска нажмите - Enter: '))
        time.sleep (1)
        br_1 = r.randint (1, 6) 
        print ('Результат: ' + Fore.RED + str(br_1) + Style.RESET_ALL)
        
        
        time.sleep (1.5)
        print ('\nБросает: ' + name_2)
        time.sleep (1)
        br_2 = r.randint (1, 6)
        print ('\nРезультат: ' + Fore.RED + str(br_2) + Style.RESET_ALL)
        
        time.sleep (1.5)
        if br_1 > br_2:
            print ('\n' + Fore.RED + name_1 + ' - Победитель.' + Style.RESET_ALL)
            time.sleep (1)
            print ('\nПоздравляю, ' + name_1 + ''', но зазнаваться не стоит. Сегодня - вы, завтра кто-то другой.''')
        elif br_1 == br_2:
            print ('\n' + Fore.RED + 'У вас - Ничья!' + Style.RESET_ALL)
        else:
            print ('\n' + Fore.RED + name_2 + ' - Победитель.' + Style.RESET_ALL)
            time.sleep (1)
            print ('\nНе нужно расстраиваться, ' + name_1 + ''', всего лишь - дело случая, 
которое ни в коем случае не занижает ваших личных качеств!''')
        
    else:
        print ('Неправильный ответ, попробуйте еще раз\n')
    time.sleep(2)    
    qw_2 = input ('''\nСыграть еще раз?
1. Да
2. Нет
''')
    print ()
    if qw_2 == "2":
        break
        
        
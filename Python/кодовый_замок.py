# КОДОВЫЙ ЗАМОК

#написать код замка
#написать ввод кода пользователем
#условия окрытия двери, либо ошибки

import time
from colorama import Fore, Back, Style # импортируем возможность менять цвет

#from colorama import init 
#init ()

code = "love"
max_try = 4
tr = 1

while True:
    print ('Количество попыток: ' + str (max_try - tr))
    enter = input ("Введите код: ")
    time.sleep (2) # откладываем вывод результата на 2 сек
    if enter == code:
        print (Fore.GREEN)
        print ("Код введен верно! Дверь открыта")
        print (Style.RESET_ALL)
    else:
        print (Fore.RED)
        print ("Код введен не верно")
        print (Style.RESET_ALL)
        
    if tr == 3:
        time.sleep (1)
        print ("Попытки кончились.")
        time.sleep (1)
        print ("Система заблокирована навсегда.")
        break
        
    time.sleep (1)
    qw = input ('''Попробовать еще раз?
1. Да
2. Нет
''')
    if qw == "2":
        break
        
    tr += 1
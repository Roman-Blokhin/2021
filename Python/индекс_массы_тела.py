# ИНДЕКС МАССЫ ТЕЛА

#ввод веса
#ввод роста в см/м
#формула
#раcчет имт + преобразование до десятков
#прописать варианты результата
#импортировать модуль time и прописать задержку времени на результат
#импортировать модуль colorama для изменения цвета текста, в зависимости от результата
#прописать исключения ошибок на ввод не чисел
#зациклить программу 

import time
from  colorama  import init
from  colorama  import  Fore ,  Back ,  Style

init()

while True:
    print ("\nТаблица индекса массы тела\n")

    try:
        a = float (input ("Введите свой вес: "))
    except ValueError:
        print(Fore.RED)
        print ("Вы ввели не число")
        print (Style.RESET_ALL)
        a = 0
        
    try:
        b = float (input ("Введите ваш рост(см): "))
    except ValueError:
        print(Fore.RED)
        print ("Вы ввели не число")
        b = 0
        
    b_1 = float (b / 100) # рост в метрах
    
    try:
        imt = a / (b_1 * b_1) # формула индекса массы тела
    except ZeroDivisionError:
        print (Fore.RED)
        print ("Результат не верен")
        print (Style.RESET_ALL)
        imt = 0
        
    imt = round (imt , 2) # сокращаем индекс до сотых
    time.sleep (1.5)
    print ("Индекс массы тела равен: " + str (imt))

    print ("\nВаш результат: ")

    if imt <= 18.5:
        time.sleep (1.5)
        print(Fore.RED)
        print ("У вас недостаток веса")
        time.sleep (1.5)
        print (Style.RESET_ALL) # сбрасывает все стили
        print ("Любить себя нужно любым(ой)! Возможно стоит пересмотреть питание и добавить в свой рацион больше белка")

    elif imt <= 24.9:
        time.sleep (1.5)
        print(Fore.GREEN)
        print ("У вас нормальный вес")
        time.sleep (1.5)
        print (Style.RESET_ALL)
        print ("Поздравляю, отличные новости! Но расслабляться не стоит, помните про правильное питание и активный образ жизни")

    elif imt <= 29.9:
        time.sleep (1.5)
        print(Fore.YELLOW)
        print ("У вас избыточный вес")
        time.sleep (1.5)
        print (Style.RESET_ALL)
        print ("Любить себя нужно любым(ой)! Но для здоровья будет не лишним правильное питание с дополнительной бытовой активностью")

    elif imt <= 34.9:
        time.sleep (1.5)
        print(Fore.RED)
        print ("У вас ожирение 1-й степени")
        time.sleep (1.5)
        print (Style.RESET_ALL)
        print ("Любить себя нужно любым(ой)! Но для здоровья рекомендую следить за питанием и добавить тренировки в зале или на свежем воздухе")

    elif imt <= 39.9:
        time.sleep (1.5)
        print(Fore.RED)
        print ("У вас ожирение 2-й степени")
        time.sleep (1.5)
        print (Style.RESET_ALL)
        print ("Любить себя нужно любым(ой)! Но для здоровья нужно обязательно пересмотреть питание, исключить сахар и мучное, а также, для начала, добавить быструю хотьбу")

    elif imt >= 40:
        time.sleep (1.5)
        print(Fore.RED)
        print ("У вас ожирение 3-й степени")
        time.sleep (1.5)
        print (Style.RESET_ALL)
        print ("Любить себя нужно любым(ой)! Но для здоровья нужно обязательно пересмотреть питание, исключить сахар и мучное, а также, для начала, добавить быструю хотьбу")
        
    time.sleep (5)
    qw = (input ("""\nПовторить расчет?
1. Да
2. Нет
"""))
    if qw == "2":
        break
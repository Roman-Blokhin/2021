# Привет, это калькулятор на зачет. Пишу его по памяти.

# запросить ввод чисел и оператора
# прописать условия по каждому оператору
# сделать повторяющийся цикл
# прописать условия выхода из программы
# прописать исключения для ввода букв, а не цифр
# прописать исключения для деления на ноль

while True: # создали цикл повторения
    try:
        a = int (input ("Введите первое число: "))
    except ValueError: 
        print ("Вы ввели не число\n")
        a = 0
        
    try:
        b = int (input ("Введите второе число: "))
    except ValueError:
        print ("Вы ввели не число")
        b = 0
        
    c = input("Выберите действие:  +, -, /, *, %, //, ** ")
    
    # условия с операторами:
    
    if c == "+":
        ans = int(a) + int(b)
        print("Ваш ответ: " + str(ans))

    elif c == "-":
        ans = int(a) - int(b)
        print("Ваш ответ: " + str(ans))

    elif c == "*":
        ans = int(a) * int(b)
        print("Ваш ответ: " + str(ans))

    elif c == "/":
        try:
            ans = int(a) / int(b)
            print("Ваш ответ: " + str(ans))
        except ZeroDivisionError:
            print("\nНеверное действие")
            ans = 0
            
    elif c == "%":
        ans = int(a) % int(b)
        print("Ваш ответ: " + str(ans))

    elif c == "//":
        ans = int(a) // int(b)
        print("Ваш ответ: " + str(ans))

    elif c == "**":
        ans = int(a) ** int(b)
        print("Ваш ответ: " + str(ans))

    # условия выхода:
    
    qw = input("Посчитаем еще? (да/нет)")
    if qw == "lf" or qw == "да" or qw == "yes":
        print(" ")      
    elif qw == "no" or qw == "ytn" or qw == "нет":
        print ("\nКонец программы.")
        break
    else:
        while True: # условия повтора вопроса при ошибке:
            qwe = input("Посчитаем еще? (да/нет)")
            if qw == "lf" or qw == "да" or qw == "yes":
                print(" ")      
            elif qw == "no" or qw == "ytn" or qw == "нет":
                print ("\nКонец программы.")
            break

    
            
    

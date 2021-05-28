# Привет, это калькулятор на зачет. Пишу его по памяти.

# запросить ввод чисел и оператора
# прописать условия по каждому оператору
# сделать повторяющийся цикл
# прописать условия выхода из программы

while True: # создали цикл повторения
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
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
        ans = int(a) / int(b)
        print("Ваш ответ: " + str(ans))

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

    
            
    

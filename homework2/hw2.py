while True:
    try:
        a = input("Введите первое целое число или слово'stop' для выхода: ")
        if a.lower() == "stop":
            print("Выход из программы.")
            break
        num1 = int(a)
        
        b = input("Введите второе целое число или слово 'stop' для выхода: ")
        if b.lower() == "stop":
            print("Выход из программы.")
            break
        num2 = int(b)
        
        print("Сумма:", num1 + num2)
    except ValueError:
        print("Ошибка! Введите целое число.")

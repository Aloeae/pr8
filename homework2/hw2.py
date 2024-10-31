while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        print("Сумма:", a + b)
    except ValueError:
        print("Ошибка! Введите целое число.")

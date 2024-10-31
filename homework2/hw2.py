while True:
    try:
        a = int(input("Введите первое целое число: "))
        b = int(input("Введите второе целое число: "))
        print("Сумма:", a + b)
    except ValueError:
        print("Ошибка! Введите целое число.")

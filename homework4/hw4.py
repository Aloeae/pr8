def get_num(num):
    while True:
        try:
            return float(input(num))
        except ValueError:
            print("Ошибка! Пожалуйста, введите число.")

a = get_num("Введите число a: ")
b = get_num("Введите число b: ")

if a < b:
    start = int(a) + 1  
    end = int(b)
    if b > end:
        end += 1
else:
    start = int(b) + 1  
    end = int(a)
    if a > end:
        end += 1

if start < end:
    print("Целые числа между", a, "и", b, ":")
    for i in range(start, end):
        print(i, end = " ")
else:
    print("Между числами нет других целых чисел.")

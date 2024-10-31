s = 0

while True:
    a = input("Введите число для подсчёта суммы. Для завершения введите слово 'stop' или 'end': ")
    if a.lower() in ["stop", "end"]:
        break  
    try:
        num = float(a)
        s += num
    except ValueError:
        print("Ошибка! Введите число.")
        continue

print("Сумма введённых чисел:", s)

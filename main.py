def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            print(f"Введено число: {value}")
            return value
        except ValueError:
            print("Ошибка: введите корректное число.")


def func1():
    a = get_float("a: ")
    a = a * a
    a = a * a
    a = a * a
    print(f"Число в 8 степени = {a}")
    return a

def func2():
    print("Вычисление M = max(x + y + z / 2, x * y * z) + 1")
    x = get_float("x: ")
    y = get_float("y: ")
    z = get_float("z: ")
    q = x + y + z / 2
    b = x * y * z
    if q > b:
        q += 1
        print("M = ", q)
    else:
        b += 1
        print("M = ", b)

def func3():
    s = 0
    for i in range(1, 51):
        s += (1 / (i ** 3))
    print(f"Сумма ряда = {s}")
    return s

while True:
        choice = input("Введите номер функции (1, 2, 3) или введите 'exit' для выхода: ")
        if choice == "1":
            result1 = func1()
            print("Возврат")
        elif choice == "2":
            func2()
            print("Возврат")
        elif choice == "3":
            result = func3()
            print("Возврат")
        elif choice.lower() == "exit":
            result = result1 + result

            print(f"Выход. {round(result, 3)}")
            break
        else:
            print("Неверно введено, попробуйте снова.")


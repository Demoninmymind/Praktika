print("Введите количество чисел, с которым нужно работать - ")
num = int(input("Количество чисел (От 1 до 4) - "))
print("Введите числа для подсчета")
if num == 2:
    a = float(input('a - '))
    b = float(input('b - '))
    f = input('Введите знак (+,-,/,*) - ')
    if f == "+":
        e = a + b                               # Сумма
        print(a, '+', b, '=', e)
    elif f == '-':
        e = a - b                               # Разность
        print(a, '-', b, '=', e)
    elif f == '/':
        e = a / b                                 # Деление
        print(a, '/', b, '=', e)
    elif f == '*':
        e = a * b                                  # Умножение
        print(a, '*', b, '=', e)
if num == 3:
    a = float(input('a - '))
    b = float(input('b - '))
    c = float(input('c - '))
    f = input('Введите знак (+,-,/,*) - ')
    if f == "+":
        e = a + b + c                                 # Сумма
        print(a, '+', b, '+', c, '=', e)
    elif f == '-':
        e = a - b - c                                 # Разность
        print(a, '-', b, '-', c, '=', e)
    elif f == '/':
        e = a / b / c                                 # Деление
        print(a, '/', b, '/', c, '=', e)
    elif f == '*':
        e = a * b * c                                 # Умножение
        print(a, '*', b, '*', c, '=', e)
if num == 4:
    a = float(input('a - '))
    b = float(input('b - '))
    c = float(input('c - '))
    d = float(input('d - '))
    f = input('Введите знак (+,-,/,*) - ')
    if f == "+":
        e = a + b + c + d                             # Сумма
        print(a, '+', b, '+', c, '+', d, '=', e)
    elif f == '-':
        e = a - b - c - d                              # Разность
        print(a, '-', b, '-', c, '-', d, '=', e)
    elif f == '/':
        e = a / b / c / d                               # Деление
        print(a, '/', b, '/', c, '/', d, '=', e)
    elif f == '*':
        e = a * b * c * d                                # Умножение
        print(a, '*', b, '*', c, '*', d, '=', e)
if num == 1:
    a = float(input('a - '))
    f = input('Введите действие (степень/корень) прошу отметить, что писать необходимо слово в слово - ').strip().lower()
    if f == ("степень" or "Степень"):
        step = int(input('Степень - '))
        e = a ** step                           # Степень
        print(a, 'в степени', step, '=', e)
    elif f == ("корень" or 'Корень'):
        e = a ** 0.5                           # Квадратный корень
        print('Квадратный корень числа', a, '=', e)
1
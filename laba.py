print('Введите коэффициенты A, B, C')
a, b, c = float(input()), float(input()), float(input())
print('Ваше уравнение (', a, ') * x**2 + (', b, ') * x + (', c, ')')
d = b ** 2 - 4 * a * c
if a == 0:
    print("X = ", -c / b)
elif d > 0:
    print('X1 = ', (-b - d ** 0.5) / (2 * a), 'X2 = ', (-b + d ** 0.5) / (2 * a))
elif d == 0:
    print('X1 = X2 = ', -b / (2 * a))
elif d < 0:
    print('Корней нет')
    
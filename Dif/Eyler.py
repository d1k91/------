import numpy as np
import matplotlib.pyplot as plt


def foo(f, x0, y0, h, n):
    """
    Реализация метода Эйлера для решения системы ОДУ.

    Аргументы:
    - f: функция, правая часть системы дифференциальных уравнений.
    - x0, y0: начальные условия.
    - h: шаг интегрирования.
    - n: количество шагов.

    Возвращает:
    - x: массив значений x.
    - y: массив значений y, решения системы ОДУ.
    """
    x = [x0]
    y = [y0]

    for i in range(1, n + 1):
        x.append(x[i - 1] + h)
        y_new = y[i - 1] + h * f(x[i - 1], y[i - 1])
        y.append(y_new)

    print('Эйлер:')
    return np.round(np.array(y[-1]), 4)







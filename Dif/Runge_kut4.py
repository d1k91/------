import numpy as np
import matplotlib.pyplot as plt


def foo(f, x0, y0, h, n):
    """
    Реализация метода Рунге-Кутта четвертого порядка для решения системы ОДУ.

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
    print('Рунге-Кут 4 порядка')
    for i in range(1, n + 1):
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + h / 2, y[i - 1] + h / 2 * k1)
        k3 = f(x[i - 1] + h / 2, y[i - 1] + h / 2 * k2)
        k4 = f(x[i - 1] + h, y[i - 1] + h * k3)

        y_new = y[i - 1] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

        x.append(x[i - 1] + h)
        y.append(y_new)

        print(f"Step {i}:")
        print(f"k1: {k1}")
        print(f"k2: {k2}")
        print(f"k3: {k3}")
        print(f"k4: {k4}")
        print(f"y_{i + 1}:", y_new)
        print()

    return np.round(np.array(y[-1]), 4)



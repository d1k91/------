import numpy as np

def f(x0, y0, h, func, x_end):
    x = [x0]
    y = [y0]
    i = 0
    while x0 + (i+1)*h <= x_end:
        k1 = func(x[i], y[i])
        k2 = func(x[i] + h/2, y[i] + h/2 * k1)
        k3 = func(x[i] + h / 2, y[i] + h / 2 * k2)
        k4 = func(x[i] + h, y[i] + h * k3)

        y_new = y[i - 1] + h/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        
        x.append(np.round(x[i] + h, 8))
        y.append(np.round(y_new, 8))
        i += 1

        # print(f"Step {i}:")
        # print(f"k1: {k1}")
        # print(f"k2: {k2}")
        # print(f"k3: {k3}")
        # print(f"k4: {k4}")
        # print(f"y_{i + 1}:", np.round(y_new, 5))
        # print()
        
    return np.round(x, 8), np.round(y, 8)
        
def func(x, y):
    return np.round(np.array([y[1], np.exp(x)]), 8)

x0 = 0  # начальное значение x
y0 = np.array([1, 1])  # начальные значения y1 и y2
h = 0.1
n = 5
x_end = 1

y = f(x0, y0, h, func, x_end)
# for i in range(len(y)):
#     print(i, y[i])
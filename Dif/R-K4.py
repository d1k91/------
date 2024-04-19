import numpy as np

def f(x0, y0, n, h, func):
    x = [x0]
    y = [y0]
    
    for i in range(1, n+1):
        k1 = func(x[i-1],y[i-1])
        k2 = func(x[i-1] + h/2, y[i-1] + h/2 * k1)
        k3 = func(x[i - 1] + h / 2, y[i - 1] + h / 2 * k2)
        k4 = func(x[i - 1] + h, y[i - 1] + h * k3)

        y_new = y[i - 1] + h/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        
        x.append(round(x[i - 1] + h, 5))
        y.append(np.round(y_new, 5))

        # print(f"Step {i}:")
        # print(f"k1: {k1}")
        # print(f"k2: {k2}")
        # print(f"k3: {k3}")
        # print(f"k4: {k4}")
        # print(f"y_{i + 1}:", np.round(y_new, 5))
        # print()
        
    return y[-1]
        
def func(x, y):
    return np.round(np.array([y[1], x * y[1] + y[0]]), 5)

# x0 = 1  # начальное значение x
# y0 = np.array([2, -1])  # начальные значения y1 и y2
# h = 0.2
# n = 5

# y = f(x0, y0, n, h, func)
# for i in range(len(y)):
#     print(i, y[i])
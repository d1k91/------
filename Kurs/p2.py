import numpy as np

def f(x0, y0, h, func, x_end):
    x = [x0]
    y = [y0]
    i = 0
    while x0 + (i+1)*h <= x_end:
        y_lined = np.round(y[i] + h * func(x[i], y[i]), 8)
        y_new = np.round(y[i] + h/2 * (func(x[i], y[i]) + func(x[i]+h, y_lined)), 8)
        
        x.append(x[i] + h)
        y.append(y_new)
        
        i+=1
        # print(f'__\ny{i+1} = {y_lined}')
        # print(f'y{i+1} = {y_new}\n')
    return np.round(x, 8), np.round(y, 8)
        

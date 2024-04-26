import Eyler as ey
import RK2pr as rk2pr
import RK2vr as rk2v
import RK4 as rk4
import numpy as np


x0 = 0 # начальное значение x
y0 = np.array([1,1])  # начальные значения y1 и y2
h = 0.2  # шаг интегрирования
n = 1  # количество шагов
mas = [rk4.f,rk4.f,rk4.f,rk4.f,rk4.f]

def main():
    test(f, y0)

def test(f_orig, y0):
    y = y0
    x = x0
    count = 0
    for foo in mas:
        x, y = foo(x, y, n, h, f_orig)
        print(f'y = {y}')
        inp = input('Сходится? 1 - да, 0 - нет\n')
        if inp == '0':
            print('Введите свое значение: ')
            for i in range(len(y)):
                y[i] = float(input(f'y[{i}] = '))
            print(y)
        else:
            count += 1
    print(f'Правильно решено {count} шагов')

def f(x, y):
    return np.array([y[1], (np.exp(x) + y[0] + y[1])/3])

if __name__ == '__main__':
    main()
import Eyler as ey
import Runge_kut2_proizv as rk2pr
import Runge_kut2_vrem as rk2v
import Runge_kut4 as rk4
import numpy as np


x0 = 1  # начальное значение x
y0 = np.array([2, -1])  # начальные значения y1 и y2
h = 0.2  # шаг интегрирования
n = 1  # количество шагов
mas = [ey.foo, rk2pr.foo, rk2v.foo, rk4.foo]

def main():
    # for foo in mas:
    #     y = foo(f, x0, y0, h, 3)
    #     print(f'{y}\n')
    test(f, mas)



def test(f_orig, mas):
    y = y0
    i = 0
    for foo in mas:
        y = foo(f_orig, x0 + h*i, y, h, n)
        i+=1
        print(f'y = {y}.')
        inp = input('Сходится? 1 - да, 0 - нет\n')
        if inp == '0':
            print('Введите свое значение: ')
            for i in range(len(y)):
                y[i] = float(input(f'y[{i}] = '))
            print(y)
        else:
            pass


def f(x, y):
    return np.array([y[1], x * y[1] + y[0]])

if __name__ == '__main__':
    main()
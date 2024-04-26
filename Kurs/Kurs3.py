import numpy as np
import p2
import p4

x0 = 0
h = 0.1
x_end = 1
n = 4
eps = 10**-4
y0 = np.array([1,1])


def main():
    recount(h, 4)

def recount(h, p):
    match p:
        case 2:
            x1, y1 = p2.f(x0, y0, h, func, x_end)
            x2, y2 = p2.f(x0, y0, h/2, func, x_end)
            print(f'\nh = {h}')
            for i in range(len(x1)):
                print(f'x = {x1[i]:<4.6f}   y = {y1[i][0]:.8f}   y\' = {y1[i][1]:.8f}')
            print(f'\nh = {h/2}')
            for i in range(len(x2)):
                print(f'x = {x2[i]:<4.6f}   y = {y2[i][0]:.8f}   y\' = {y2[i][1]:.8f}')
            
            for i in range(len(x1)):
                if abs(y1[i][0] - y2[2*i][0]) >= 3 * eps:
                    recount(h/2, 2)
                else:
                    pass
        case 4:
            x1, y1 = p4.f(x0, y0, h, func, x_end)
            x2, y2 = p4.f(x0, y0, h/2, func, x_end)
            print(f'\nh = {h:.10}')
            # for i in range(len(x1)):
            #     print(f'x = {x1[i]:<4.6f}   y = {y1[i][0]:.8f}   y\' = {y1[i][1]:.8f}')
            # print(f'\nh = {h/2}')
            # for i in range(len(x2)):
            #     print(f'x = {x2[i]:<4.6f}   y = {y2[i][0]:.8f}   y\' = {y2[i][1]:.8f}')
            
            for i in range(len(x1)):
                if abs(y1[i][0] - y2[2*i][0]) >= 15 * eps:
                    print(f'{y1[i][0] - y2[2*i][0]}, да')
                    recount(h/2, 4)
                else:
                    print('нет')
                    pass
            
    

def func(x, y):
    return np.array([y[1], np.exp(x)])















if __name__ == '__main__':
    main()
import numpy as np

x0 = 1
n = 10
h = 0.1
def main():
    print(trap(func_trap, h, n, x0))
    print(Simpson(func_simps, x0, h, n))


def trap(f, h,n,x0):
    x = np.linspace(x0, x0 + (n-1)*h, n)
    y = f(x)
    integral = (y[0] + y[-1])/2
    for i in range(1,n):
        integral += y[i]
    integral *= h
    return integral


def Simpson(f,x0,h,n):
    if n % 2 != 0:
        raise ValueError('n должно быть четным')
    x = np.linspace(x0, x0 + (n-1)*h, n)
    y = f(x)   
    integral = h/3 * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]) + y[-1])

    return h/3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]))


def func_simps(x):
    return np.round(x**2 + 3*x ,4)

def func_trap(x):
    return 1/x


if __name__ == '__main__':
    main()
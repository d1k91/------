import numpy as np

x0 = 1
n = 10
h = 0.1
def main():
    print(trap(func_trap, h, n, x0))
    #print(Simpson(func_simps, x0, h, n))


def trap(f, h,n,x0):
    x = np.round(np.linspace(x0, x0 + (n)*h, n+1), 4)
    y = np.round(f(x), 4)
    res = 0
    for i in range(0,len(x)-1,1):
        res += integral_T(x,y,i)    
    return round(res,4)


def Simpson(f,x0,h,n):
    if n % 2 != 0:
        raise ValueError('n должно быть четным')
    res = 0
    x = np.linspace(x0, x0 + (n)*h, n+1)
    x= np.round(x,4)
    y = f(x)
    y = np.round(y,4)
    for i in range(0,len(x)-2,2):
        res += integral_S(x,y,i)
        
    return res

def integral_S(x,y,i):
    print(f"{int(i/2 + 1)}.  ", round((x[i+2]-x[i])*(1/6 * y[i] + 2/3*y[i+1] + 1/6*y[i+2]),4))
    #print(f"({x[i+2]}-{x[i]})*(1/6 * {y[i]} + 2/3*{y[i+1]} + 1/6*{y[i+2]})")
    return round((x[i+2]-x[i])*(1/6 * y[i] + 2/3*y[i+1] + 1/6*y[i+2]),4)

def integral_T(x,y,i):
    a = (x[i+1]-x[i])*(1/2 * y[i] + 1/2*y[i+1])
    print(f"{int(i + 1)}.  ", round(a,4))
    # print(f"({x[i+1]}-{x[i]})*(1/2 * {y[i]} + 1/2*{y[i+1]})")
    return a

def func_simps(x):
    return 1/x

def func_trap(x):
    return 1/x


if __name__ == '__main__':
    main()
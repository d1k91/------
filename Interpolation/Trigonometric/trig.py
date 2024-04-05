import numpy as np
import matplotlib.pyplot as plt

point = 8
x0 = 2
h = 4
n = 4

def main():
    
    x,y = init(x0, h, n)
    print(find_y(point, x0, n, h, y))
    #graph(x,y)

def func(x):
    return round(x**2)
    
def init(x0, h, n):
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i] = round(x0 + i * h, 4)
        y[i] = func(x[i])
    return x,y

def A(j, y, n):
    a = 0
    i = 1j
    for k in range(n):
        a += y[k] * (round(np.cos(-2 * np.pi * (k*j)/n), 4) + i * round(np.sin(-2 * np.pi * (k*j)/n), 4))
        #print(y[k], round(np.cos(-2 * np.pi * (k*j)/n), 4) + i * round(np.sin(-2 * np.pi * (k*j)/n), 4))
        
    if j == 0:
        return a
    else:
        return a * 1/n
    
def find_y(x, x0, n, h, y):
    yx = 0
    i = 1j
    for j in range(int(-n/2)+1, int(n/2)+1):
        yx += A(j,y,n) * (round(np.cos(2*np.pi*j*((x-x0)/(n*h))), 4) + i * round(np.sin(2*np.pi*j*((x-x0)/(n*h))), 4))
        #print(A(j,y,n) * (round(np.cos(2*np.pi*j*((x-x0)/(n*h))), 4) + i * round(np.sin(2*np.pi*j*((x-x0)/(n*h))), 4)))
    return np.round(yx, 4)


def graph(x, y):
    xr = [0]*((int(x[-1])-int(x[0]))*10)
    yr = [0]*((int(x[-1])-int(x[0]))*10)
    for i in range((int(x[-1])-int(x[0]))*10):
        xr[i] = x[0] + i * 0.1
        yr[i] = func(xr[i])
    
    for i in range(len(x)):
        if x[i] > point:
            y = y[0:i] + [find_y(point,x0,n,h,y)] + y[i:]
            x = x[0:i] + [point] + x[i:]
    
    plt.plot(xr,yr, "r--")
    plt.plot(x,y, "b")
    plt.show()
    
    

if __name__ == "__main__":
    main()
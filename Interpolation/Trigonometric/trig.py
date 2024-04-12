import numpy as np
import matplotlib.pyplot as plt

point = 1.5
x0 = 0
h = 1
n = 4
coef = 10

def main():
    
    x,y = init(x0, h, n)
    print(f"{x}\n{y}")
    print(find_y(point, x0, n, h, y))
    graph(x,y)

def graph(x, y):
    s = [0] * int((n-1) * coef)
    i = 0
    re = [0] * int((n-1) * coef)
    im = [0] * int((n-1) * coef)
    y_orig = [0] * int((n-1) * coef)
    for i in range(len(s)):
        s[i] = round((x[0] + 1 * (h/2) + h*i) / coef, 4)
        xx = find_y(s[i], x0, n, h, y)
        re[i] = xx.real
        im[i] = xx.imag
        y_orig[i] = func(s[i])
        print(s[i], y_orig[i])
        
    

    figure, axis = plt.subplots(2,2)
    
    
    figure.set_size_inches(9,7)
    
    axis[0,0].plot(re,im)
    axis[0,0].set_title('Re/Im')
    
    axis[0,1].plot(s,re)
    axis[0,1].set_title('x/Re')
    
    axis[1,0].plot(s,im)
    axis[1,0].set_title('x/Im')
    
    axis[1,1].plot(s,y_orig)
    axis[1,1].set_title('Original')
    
    plt.show()
        
        

def func(x):
    return round(x**2, 4)
    
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
        
    return a
    
def find_y(x, x0, n, h, y):
    yx = 0
    i = 1j
    for j in range(int(-n/2)+1, int(n/2)+1):
        #yx += A(j,y,n) * (round(np.cos(2*np.pi*j*((x-x0)/(n*h))), 4) + i * round(np.sin(2*np.pi*j*((x-x0)/(n*h))), 4))
        yx += A(j,y,n) * np.exp(2 * np.pi * i * j * ((x-x0)/(n*h)))
        #print(A(j,y,n) * (round(np.cos(2*np.pi*j*((x-x0)/(n*h))), 4) + i * round(np.sin(2*np.pi*j*((x-x0)/(n*h))), 4)))
    yx *= 1/n
    return np.round(yx, 4)
    

if __name__ == "__main__":
    main()
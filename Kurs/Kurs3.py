import numpy as np
import p2
import p4

x0 = 0
h = 0.9
x_end = 1
eps = 10**-4
y0 = np.array([1,1])
count = 0
def func(x, y):
    return np.array([y[1], np.exp(x)])

def main():
    rec(h,4)  

def rec(h, p):
    global count
    match p:
        case 2:
            x1, y1 = p2.f(x0,y0,h,func,x_end)
            x2, y2 = p2.f(x0,y0,h/2,func,x_end)
            print(f'\nh = {h}')
            for i in range(len(x1)):
                check = abs(y1[i][0] - y2[2*i][0])>3*eps
                #print(f'x = {x1[i]:<6.10}, y1 = {y1[i][0]:<10.10}, y2 = {y2[2*i][0]:<10.10}, Δ = {abs(y1[i][0] - y2[2*i][0]):<10.10} {check}')
                print(f'x = {x1[i]:<10.10} | y = {y1[i][0]:<10.10} | y\' = {y1[i][1]:<10.10}')
                if check == True:
                    count = 0
                    rec(h/2, 2)
                else:
                    count += 1
                    if count == len(x1):
                        #print(f'\nx = {x1[i]:<10.10} | y = {y1[i][0]:<10.10} | y\' = {y1[i][1]:<10.10}')
                        quit()
                        
        case 4:
            x1, y1 = p4.f(x0,y0,h,func,x_end)
            x2, y2 = p4.f(x0,y0,h/2,func,x_end)
            print(f'\nh = {h}')
            for i in range(len(x1)):
                check = abs(y1[i][0] - y2[2*i][0]) > 15*eps
                #print(f'x = {x1[i]:<10.10}, y1 = {y1[i][0]:<10.10}, y2 = {y2[2*i][0]:<10.10}, Δ = {abs(y1[i][0] - y2[2*i][0]):<10.10} {check}')
                print(f'x = {x1[i]:<10.10} | y = {y1[i][0]:<10.10} | y\' = {y1[i][1]:<10.10}')
                if check == True:
                    count = 0
                    rec(h/2, 4)
                else:
                    count += 1
                    if count == len(x1):
                        #print(f'\nx = {x1[i]:<10.10} | y = {y1[i][0]:<10.10} | y\' = {y1[i][1]:<10.10}')
                        quit()


















if __name__ == '__main__':
    main()
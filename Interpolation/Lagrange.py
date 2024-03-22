import matplotlib.pyplot as plt
import math

data = [2.56]

def main():
    x, y = init()
    print(Lagrange(x, y, 2.56))
    print(Eytken(x, y, 5, 2.56))
    print(newton_interpolation(2.56, x,y))
    print(newton(2.56, x, y))
    for i in range(7):
        print(i, math.sin(i))
    for_graph(x,y, 4)
    

def print_tabl(delta):
    for i in range(len(delta)):
        for j in range(len(delta[i])):
            if delta[i][j] == None:
                delta[i][j] = 0.0
            print(f"{delta[i][j]:>7.3}", end=' ')
        print(' ')
    
def divided_differences(x_values, y_values):
    n = len(x_values)
    F = [[None] * n for _ in range(n)]

    for i in range(n):
        F[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x_values[i + j] - x_values[i])
    #print_tabl(F)
    return F[0]

def newton_interpolation(x, x_values, y_values):
    coeffs = divided_differences(x_values, y_values)
    n = len(x_values)
    interpolation = coeffs[0]
    for i in range(1, n):
        term = coeffs[i]
        for j in range(i):
            term *= (x - x_values[j])
        interpolation += term
    return round(interpolation, 5)

def newton(x, x_val, y_val):
    n = len(x_val)
    F = [[None] * n for _ in range(n)]

    for i in range(n):
        F[i][0] = y_val[i]

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x_val[i + j] - x_val[i])
    #print_tabl(F)
    interpolation = F[0][0]
    for j in range(1, n):
        term = F[0][j]
        for i in range(j):
            term *= (x - x_val[i])
        interpolation += term

    return round(interpolation, 5)
    
def Lagrange(x, y, point):
    n = len(x)
    res = 0.0
    for i in range(n):
        g = y[i]
        for j in range(n):
            if j != i:
                g *= (point - x[j])/(x[i] - x[j])
        res += g
    return round(res, 5)    
    

def Eytken(x, y, n, point):
    m = n
    P = y[0:n+1]
    for j in range(m):
        for i in range(m): 
            if i +j+ 1 <= n:
                P[i] = (P[i]*(point - x[i+j+1]) - P[i+1]*(point - x[i]))/(x[i] - x[i+j+1])
        m -= 1     
    return round(P[0], 5)    
       

    
def init():
    with open("D:/vich/Interpolation/nums.txt", "r") as f:
        nums = f.readlines()
        n = len(nums)
        x = [0] * n
        y = [0] * n
        print(x)
        for i in range(n):
            raw = nums[i].split()
            x[i] = float(raw[0])
            y[i] = float(raw[1])
    return x, y
            
            
def for_graph(x,y, n = None):
    # if n == None:
    #     for i in data:
    #         y.append(Lagrange(x,y,i))
    #         x.append(i)
        
    #     for j in range(len(x)):
    #         if x[j] in data:
    #             plt.scatter(x[j], y[j], c = "red", s = 15)
    #         else:
    #             plt.scatter(x[j], y[j], c = "blue", s = 15)
    #     plt.show()
        
        
    # else:
    #     for i in data:
    #         y.append(Eytken(x,y,n,i))
    #         x.append(i)
            
    #     y_r = y[0:n]
    #     x_r = x[0:n]
    #     x_r.append(x[-1])
    #     y_r.append(y[-1])
        
    #     for j in range(n+1):
    #         if x_r[j] in data:
    #             plt.scatter(x_r[j], y_r[j], c = "red", s = 15)
    #         else:
    #             plt.scatter(x_r[j], y_r[j], c = "blue", s = 15)
    #     plt.show()
    
    for i in data:
        y.append(newton(i,x,y))
        x.append(i)
    x.sort()
    y.sort()
    y_r=[0]*len(y)
    x_r=[0]*len(x)
    for i in range(1, len(y)+1):
        x_r[i-1] = i
        y_r[i-1] = math.sin(i)
    plt.plot(x_r, y_r, color='red')
    plt.plot(x, y, color='blue')
    plt.show()
                


if __name__ == "__main__":
    main()
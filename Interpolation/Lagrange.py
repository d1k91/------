import matplotlib.pyplot as plt
import math

data = [2.56]
#ax = plt.gca()
#ax.spines['bottom'].set_position('center')
#ax.spines['top'].set_visible(False)
#ax.spines['right'].set_visible(False)


def main():
    x, y = init()
    print(Lagrange(x, y, data[0]))
    print(Eytken(x, y, len(x)-1, data[0]))
    print(newton_interpolation(data[0], x,y))
    print(newton(data[0], x, y))
    graph(x,y)

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

def newton_interpolation(point, x, y):
    coeffs = divided_differences(x, y)
    n = len(x)
    interpolation = coeffs[0]
    for i in range(1, n):
        term = coeffs[i]
        for j in range(i):
            term *= (point - x[j])
        interpolation += term
    return round(interpolation, 5)

def newton(point, x, y):
    n = len(x)
    F = [[None] * n for _ in range(n)]

    for i in range(n):
        F[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])
    #print_tabl(F)
    interpolation = F[0][0]
    for j in range(1, n):
        term = F[0][j]
        for i in range(j):
            term *= (point - x[i])
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
    with open("F:/4 семак/вычмат/VichMat/------/Interpolation/nums.txt", "r") as f:
        nums = f.readlines()
        n = len(nums)
        x = [0] * n
        y = [0] * n
        for i in range(n):
            raw = nums[i].split()
            x[i] = float(raw[0])
            y[i] = float(raw[1])
    return x, y
                
                
def graph(x,y):
    x_r = [0]*(int(x[-1])*10)
    y_r = [0]*(int(x[-1])*10)
    x_e = x_l = x_n1 = x_n2 = x
    y_e = y_l = y_n1 = y_n2= y
    for i in range(int(x[-1])*10):
        x_r[i] = (i+1)/10
        y_r[i] = math.sin((i+1)/10)
    
    for i in range(1,len(x)):
        if x[i] > data[0]:
            y_l = y_l[0:i] + [Lagrange(x_l, y_l, data[0])] + y_l[i:]
            x_l = x_l[0:i] + [data[0]] + x_l[i:]
            
            y_e = y_e[0:i] + [Eytken(x_e, y_e, len(x_e)-1, data[0])] + y_e[i:]
            x_e = x_e[0:i] + [data[0]] + x_e[i:]
            
            y_n1 = y_n1[0:i] + [newton(data[0], x_l, y_l)] + y_n1[i:]
            x_n1 = x_n1[0:i] + [data[0]] + x_n1[i:]
            
            y_n2 = y_n2[0:i] + [newton_interpolation(data[0], x_n2, y_n2)] + y_n2[i:]
            x_n2 = x_n2[0:i] + [data[0]] + x_n2[i:]
            break
                
    
    #plt.plot(x_l,y_l,"bo", linewidth=2.0, label = "Lagrange")
    #plt.plot(x_e,y_e,"yo", linewidth=2.0, label = "Eytken")
    #plt.plot(x_n1,y_n1,"go", linewidth=2.0, label = "Newton1")
    #plt.plot(x_n2,y_n2, "co", linewidth=2.0, label = "Newton2")
    plt.plot(x_r,y_r,"r--", linewidth=2.0, label = "Function")
    plt.legend()
    plt.show()

    

if __name__ == "__main__":
    main()
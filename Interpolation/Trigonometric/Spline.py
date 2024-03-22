import Gauss
import matplotlib.pyplot as plt

def main():
    x,y = init()
    print(x, y, "\n")
    C,d = find_C(x,y)
    for i in range(len(C)):
        print(C[i])
    print("\n",d)
    M = Gauss.gauss_method(C,d)
    M = [0] + M + [0]
    S = find_s(x,y,M,1.1)
    graph(x,y,M)
    

def graph(x,y,m):
    plt.plot(x, y)
    x_r = [0]*(int(x[-1])*10)
    y_r = [0]*(int(x[-1])*10)
    for i in range(10, int(x[-1])*10):
        x_r[i] = i/10
        y_r[i] = find_s(x, y, m, i/10)
        print(x_r[i], y_r[i])
    plt.plot(x_r, y_r)
    plt.show()
    


def find_s(x,y,M, point):
    s = 0
    i = 0
    for k in range(len(x)):
        if x[k] > point:
            i = k
            break
    s += M[i-1]*((x[i]-point)**3)/(6*(x[i]-x[i-1]))
    s += M[i]*((point-x[i-1])**3)/(6*(x[i]-x[i-1]))
    s += (y[i-1] - (M[i-1]*(x[i]-x[i-1])**2)/6)*((x[i]-point)/(x[i]-x[i-1]))
    s += (y[i] - (M[i]*(x[i]-x[i-1])**2)/6)*((point-x[i-1])/(x[i]-x[i-1]))
    return s
    
    
def find_C(x,y):
    C = [0] * 3
    d = [0] * 3
    for i in range(3):
        C[i] = [0] * 4
    
    for i in range(3):
        for j in range(4):
            if i == j:
                h1 = x[i] - x[i-1]
                h2 = x[i+1] - x[i]
                C[i][j] = (h1+h2)/3
            elif j == i + 1:
                h = x[i+1] - x[i]
                C[i][j] = h/6
            elif j == i - 1:
                h = x[i] - x[i-1]
                C[i][j] = h/6
            elif abs(j-1) > 1:
                C[i][j] = 0
    for i in range(1,len(y)-1):
        d[i-1] = ((y[i+1]-y[i])/(x[i+1] - x[i])) - ((y[i]-y[i-1])/x[i]-x[i-1])
    return C,d

def init():
    with open("F:/4 семак/вычмат/VichMat/------/Interpolation/Trigonometric/nums.txt", "r") as f:
        nums = f.readlines()
        n = len(nums)
        x = [0] * n
        y = [0] * n
        for i in range(n):
            raw = nums[i].split()
            x[i] = float(raw[0])
            y[i] = float(raw[1])
    return x, y


if __name__ == "__main__":
    main()
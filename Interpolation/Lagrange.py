import matplotlib.pyplot as plt

data = [2.56]

def main():
    x, y = init()

    #for_graph(x,y)
    print(Lagrange(x, y, 2.56))
    
    print(Eytken(x, y, 5, 2.56))
    
    
def for_graph(x,y):
    for i in data:
        y.append(Lagrange(x,y,i))
        x.append(i)
    
    for j in range(len(x)):
        if x[j] in data:
            plt.scatter(x[j], y[j], c = "red", s = 15)
        else:
            plt.scatter(x[j], y[j], c = "blue", s = 15)
    plt.show()
    
    
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
        print(x)
        for i in range(n):
            raw = nums[i].split()
            x[i] = float(raw[0])
            y[i] = float(raw[1])
    return x, y
            

if __name__ == "__main__":
    main()
import math


def f1(x, y):
    return x**2 + y**2  -13

def f1_px(x):
    return 2*x

def f2(x,y):
    return x*y-4


def main():
    nums, l, v_nums, lv = readfiles()
    nums = tofloat(nums)
    v_nums = tofloat(v_nums)
    
    if math.sqrt(l) % 1 != 0:
        print('Не получится построить квадратную матрицу')
        exit()
    if int(math.sqrt(l)) != lv:
        print('Количесвто свободных ченов не совпадает с количеством переменных')
        exit()

    else:
        pass



def tofloat(list):
    for i in range(len(list)):
        list[i] = float(list[i])
    return list

def readfiles():
    with open('D:/ВычМат/MPI/matrix_mpi.txt','r') as f:
        nums = f.readlines()
        l = len(nums)
        if l == 1:
            nums = nums[0].split(' ')
            l = len(nums)
    
    with open('D:/ВычМат/MPI/vector_mpi.txt','r') as fv:
        vetor_nums = fv.readlines()
        lv = len(vetor_nums)
        if lv == 1:
            vetor_nums = vetor_nums[0].split(' ')
            lv = len(vetor_nums)
    
    return nums, l, vetor_nums, lv

def init(n, nums):
    matrix = [0]*n
    for i in range(n):
        matrix[i] = [0]*n
    k=0
    for i in range(0,n):
        for j in range(0,n):
            matrix[i][j] = nums[k]
            k+=1
    return matrix

def print_matrix(matrix=None, v_nums=None):
    if matrix != None and v_nums != None:
        n = len(matrix)
        print('')
        for i in range(0,n):
            for j in range(0,n):
                print( f"{matrix[i][j]:>7.3f}", end=' ')
            print(f'| {v_nums[i]:>7.3f}', end='\n')
    
    if matrix != None and v_nums == None:
        n = len(matrix)
        print('')
        for i in range(0,n):
            for j in range(0,n):
                print( f"{matrix[i][j]:>7.3f}", end=' ')
            print('')

def print_vector(vector):
    n = len(vector)
    print('')
    for i in range(n):
        if vector[i] < 0.0000001:
            print(f'{abs(vector[i]):>7.3f}', end='\n')
        else:
            print(f'{vector[i]:>7.3f}', end='\n')






if __name__ == '__main__':
    main()
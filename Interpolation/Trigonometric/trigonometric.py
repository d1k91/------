
def main():
    x, y = init()
    print(x,y)



def init():
    with open("D:/vich/Interpolation/Trigonometric/nums.txt", "r") as f:
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
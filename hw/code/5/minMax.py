import random as r

# Check input constraints
def okx1x2(x):
    if x[1] + x[2] - 2 < 0 :
        return False
    if 6 - x[1] - x[2] < 0:
        return False
    if 2 - x[2] + x[1] < 0:
        return False
    if 2 - x[1] + 3 * x[2] < 0:
        return False
    return True

def okx3x4(x):
    if 4 - (x[3] - 3) ** 2 - x[4] < 0:
        return False
    return True

def okx5x6(x):
    if (x[5] - 3) ** 3 + x[6] - 4 < 0:
        return False
    return True

def f1(x):
    return -1 * (25 * (x[1] - 2) ** 2 + (x[2] - 2) ** 2 + (x[3] - 1) ** 2 * (x[4] - 4) ** 2 + (x[5] - 1) ** 2)

def f2(x):
    return x[1] ** 2 + x[2] ** 2 + x[3] ** 2 + x[4] ** 2 + x[5] ** 2 + x[6] ** 2

# low = [0, 0, 0, 1, 0, 1, 0]
# up = [0, 10, 10, 5, 6, 5, 10]

def getRandomInputForOsyczka2():
#     Initial unsatisfaible values
    x = [0, -1, -1, -2, -1, -2, -1]

    while not okx1x2(x):
        x[1] = r.uniform(0, 10)
        x[2] = r.uniform(0, 10)

    while not okx3x4(x):
        x[3] = r.uniform(1, 5)
        x[4] = r.uniform(0, 6)

    while not okx5x6(x):
        x[5] = r.uniform(1, 5)
        x[6] = r.uniform(0, 10)

    return x

if __name__ == '__main__':
    min = 100000
    max = -100000

    for _ in range(500000):
        x = getRandomInputForOsyczka2()
        e = f1(x) + f2(x)
        if min > e:
            min = e
        if max < e:
            max = e
            
    print 'Emin: ', min
    print 'Emax: ', max

# Output:
# Emin:  -396.221369935
# Emax:  146.314249947

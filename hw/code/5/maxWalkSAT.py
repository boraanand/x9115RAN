from __future__ import print_function, division
import random as r
import math

low = [0, 0, 0, 1, 0, 1, 0]
up = [0, 10, 10, 5, 6, 5, 10]

Emin = -396.221369935
Emax = 146.314249947

p = 0.5
steps = 10
retries = 50
maxchanges = 20
threshold = 1
evals = 0

def drange(start, stop, step):
    while start < stop:
            yield start
            start += step
            
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

def getRandomInputForOsyczka2():
    global Emax
    global Emin
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

    e = f1(x) + f2(x)
    if Emin > e:
        Emin = e
    if Emax < e:
        Emax = e

    return x

def normalize(e):
    return (e - Emin) / (Emax - Emin)

def changeRandomInC(c, x, e):
    x_new = list(x)
    
    x_new[c] = r.uniform(low[c], up[c])
    ctr = 1000
    while not (okx1x2(x_new) and okx3x4(x_new) and okx5x6(x_new)):
        ctr -= 1
        if ctr == 0:
            return x, e
        x_new[c] = r.uniform(low[c], up[c])
        
    e_best = normalize(f1(x_new) + f2(x_new))
    return x_new, e_best
    
def changeCToMaximizeEnergy(c, x, e_old):
    global evals
    step = (up[c] - low[c]) / float(steps)
    x_new = list(x)
    e_best = e_old
    for i in drange(low[c], up[c], step):
        evals += 1
        x_new[c] = i
        if okx1x2(x_new) and okx3x4(x_new) and okx5x6(x_new):
            e_new = normalize(f1(x_new) + f2(x_new))
            if e_new > e_best:
                e_best = e_new
    
    if e_best == e_old:
        return x, e_old  # earlier solution was better.
    return x_new, e_best

def mws():
    global evals
    e_best = Emin
    x_best = [0, -1, -1, -2, -1, -2, -1]
    printCtr = 0

    for _ in range(retries) :
        x = getRandomInputForOsyczka2()
        e = normalize(f1(x) + f2(x))        
        for _ in range(maxchanges) :
            evals += 1
            if printCtr == 0 or printCtr % 50 == 0: 
                print ("%e" % e, end=' ') 
    
            if e > threshold:
                return x, e
            
            # c = random part of solution 
            c = r.randint(1, 6)
            if p < r.random():
                # change a random setting in c
                x_new, e_new = changeRandomInC(c, x, e)
                if e_new > e:
                    e = e_new
                    x = x_new
                    print('?', end='')
                else :
                    print('.', end='')


            else:
                # change setting in c that maximizes score(solution)
                x_new, e_new = changeCToMaximizeEnergy(c, x, e)
                if e_new > e:
                    e = e_new
                    x = x_new
                    print('+', end='')
                else :
                    print('.', end='')
            
            printCtr += 1
            if printCtr % 50 == 0: 
                print ('') 

                
            if e > e_best:
                e_best = e
                x_best = x
                
    return x_best, e_best;

if __name__ == '__main__':
    best = mws()
    print ('\nBest energy = %.4f' % best[1])
    print ('At x = [' , '%.2f' % best[0][1], ',', '%.2f' % best[0][2], ',', '%.2f' % best[0][3], ',', '%.2f' % best[0][4], ',', '%.2f' % best[0][5], ']')
    print ('Evals = ' , evals)
    
#     print ('\nBest Energy = ', best.E(), ' at x = ', best.x)

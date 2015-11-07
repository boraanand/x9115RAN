from __future__ import print_function, division
import random as r
import math
from copy import deepcopy
import sys
from math import sqrt, exp, sin

class Model(object):
    def random(i):
        while True:
            for j in range(len(i.dec)):
                i.dec[j][0] = r.uniform(i.dec[j][1], i.dec[j][2])
            if i.ok(): 
                break

    def __init__(i):
        i.dec = [0, 0, 0]  # [0][0] has dec name (example x1), [0][1] it's low, [0][2] it's high

    def getEnergy(i):
        return i.normalize(sum(i.objs()))
 
    def getDenormalizedEnergy(i):
        return sum(i.objs())

    def getobj(i):
        return []

    def ok(i):
        return True

    def decOk(i):
        for j in range(len(i.dec)):
            if not ((i.dec[j][0] >= i.dec[j][1]) and (i.dec[j][0] <= i.dec[j][2])):
                return False
            
        return True

    # Default less than
    # less than. Goal is to minimize. Return true if new < best.
    def ltOrGt(i, Enew, Ebest):
        if Enew < Ebest:
            return True
        return False

    def getMinMax(i):
        min = sys.maxint
        max = -1 * sys.maxint
        for _ in range(500000):
            i.random()
            e = sum(i.objs())
            if min > e:
                min = e
            if max < e:
                max = e
        return min, max    
    
    def __repr__(i):
        return str(zip(*i.dec)[0])

class Kursawe(Model):
     
    def __init__(i):
        i.dec = [[1, -5, 5]]
        i.dec.append([1, -5, 5])
        i.dec.append([1, -5, 5])
        i.random()
#         i.Emin, i.Emax = i.getMinMax()
 
    def normalize(i, e):
 
        if i.Emin > e:
            i.Emin = e
        if i.Emax < e:
            i.Emax = e
 
        return (e - i.Emin) / (i.Emax - i.Emin)

    def f1(i):
        total = 0
        for j in range(len(i.dec) - 1):
            e = -0.2 * sqrt(i.dec[j][0] ** 2 + i.dec[j + 1][0] ** 2)
            total += -10 * exp(e)
        return total
    
    def f2(i):
        total = 0
        for j in range(len(i.dec)):
            total += abs(i.dec[j][0]) ** 0.8 + 5 * sin(i.dec[j][0] ** 3)
        return total
         
    def objs(i):
        return [i.f1(), i.f2()]
     
class Schaffer(Model):
    
    def __init__(i):
        i.dec = [ [1, -10 ** 2, 10 ** 2] ]
        i.random()
#         i.Emin, i.Emax = i.getMinMax()

    def normalize(i, e):

        if i.Emin > e:
            i.Emin = e
        if i.Emax < e:
            i.Emax = e

        return (e - i.Emin) / (i.Emax - i.Emin)
        
    def objs(i):
        f1 = i.dec[0][0] ** 2
        f2 = (i.dec[0][0] - 2) ** 2
        return [f1, f2]
    
class Osyczka2(Model):
    def __init__(i):
        i.dec = [[-1, 0, 10]]
        i.dec.append([-1, 0, 10])
        i.dec.append([-2, 1, 5])
        i.dec.append([-1, 0, 6])
        i.dec.append([-2, 1, 5])
        i.dec.append([-1, 0, 10])
        i.random()
#         i.Emin, i.Emax = i.getMinMax()

    # Check input constraints
    def okx1x2(i):
        if i.dec[0][0] + i.dec[1][0] - 2 < 0 :
            return False
        if 6 - i.dec[0][0] - i.dec[1][0] < 0:
            return False
        if 2 - i.dec[1][0] + i.dec[0][0] < 0:
            return False
        if 2 - i.dec[0][0] + 3 * i.dec[1][0] < 0:
            return False
        return True

    def okx3x4(i):
        if 4 - (i.dec[2][0] - 3) ** 2 - i.dec[3][0] < 0:
            return False
        return True

    def okx5x6(i):
        if (i.dec[4][0] - 3) ** 3 + i.dec[5][0] - 4 < 0:
            return False
        return True

    def ok(i):
        return  i.okx1x2() and i.okx3x4() and i.okx5x6()

    def random(i):
        i.dec[0][0] = r.uniform(i.dec[0][1], i.dec[0][2])
        i.dec[1][0] = r.uniform(i.dec[1][1], i.dec[1][2])
        while not i.okx1x2():
            i.dec[0][0] = r.uniform(i.dec[0][1], i.dec[0][2])
            i.dec[1][0] = r.uniform(i.dec[1][1], i.dec[1][2])
        i.dec[2][0] = r.uniform(i.dec[2][1], i.dec[2][2])
        i.dec[3][0] = r.uniform(i.dec[3][1], i.dec[3][2])
        while not i.okx3x4():
            i.dec[2][0] = r.uniform(i.dec[2][1], i.dec[2][2])
            i.dec[3][0] = r.uniform(i.dec[3][1], i.dec[3][2])
        i.dec[4][0] = r.uniform(i.dec[4][1], i.dec[4][2])
        i.dec[5][0] = r.uniform(i.dec[5][1], i.dec[5][2])
        while not i.okx5x6():
            i.dec[4][0] = r.uniform(i.dec[4][1], i.dec[4][2])
            i.dec[5][0] = r.uniform(i.dec[5][1], i.dec[5][2])
            
    def normalize(i, e):

        if i.Emin > e:
            i.Emin = e
        if i.Emax < e:
            i.Emax = e

        return (e - i.Emin) / (i.Emax - i.Emin)


    # gt than. Goal is to minimize. Return true if new > best.
    def ltOrGt(i, Enew, Ebest):
        if Enew > Ebest:
            return True
        return False
        
    def objs(i):
        f1 = -1 * (25 * (i.dec[0][0] - 2) ** 2 + (i.dec[1][0] - 2) ** 2 + (i.dec[2][0] - 1) ** 2 * (i.dec[3][0] - 4) ** 2 + (i.dec[4][0] - 1) ** 2)
        f2 = i.dec[0][0] ** 2 + i.dec[1][0] ** 2 + i.dec[2][0] ** 2 + i.dec[3][0] ** 2 + i.dec[4][0] ** 2 + i.dec[5][0] ** 2
        return [f1, f2]

class Golinski (Model):
     
    def __init__(i):
        i.dec = [[-1, 2.6, 3.6]]
        i.dec.append([-1, 0.7, 0.8])
        i.dec.append([-1, 17.0, 28.0])
        i.dec.append([-1, 7.3, 8.3])
        i.dec.append([-1, 7.3, 8.3])
        i.dec.append([-1, 2.9, 3.9])
        i.dec.append([-1, 5.0, 5.5])

        i.random()
#         i.Emin, i.Emax = i.getMinMax()
 
    def normalize(i, e):
 
        if i.Emin > e:
            i.Emin = e
        if i.Emax < e:
            i.Emax = e
 
        return (e - i.Emin) / (i.Emax - i.Emin)

    def f1(i):
        return 0.7854 * i.dec[0][0] * (i.dec[1][0] ** 2) * (10 * (i.dec[2][0] ** 2) / 3 + 14.933 * i.dec[2][0] - 43.0934) - 1.508 * i.dec[0][0] * (i.dec[5][0] ** 2 + i.dec[6][0] ** 2) + 7.477 * (i.dec[5][0] ** 3 + i.dec[6][0] ** 3) + 0.7854 * (i.dec[3][0] * (i.dec[5][0] ** 2) + i.dec[4][0] * (i.dec[6][0] ** 2))
    
    def f2(i):
        u = (745 * i.dec[3][0] / (i.dec[1][0] * i.dec[2][0])) ** 2 + 1.69 * 10 ** 7
        d = 0.1 * i.dec[5][0] ** 3
        return u ** 0.5 / d
            
    def objs(i):
        return [i.f1(), i.f2()]

    # gt than. Goal is to minimize. Return true if new > best.
    def ltOrGt(i, Enew, Ebest):
        if Enew > Ebest:
            return True
        return False

    def ok(i):
        if 1 / (i.dec[0][0] * i.dec[0][1] ** 2 * i.dec[2][0]) - 1 / 27 > 0:
            return False
        
        if 1 / (i.dec[0][0] * i.dec[1][0] ** 2 * i.dec[2][0] ** 2) - 1 / 397.5 > 0:
            return False
        
        if i.dec[3][0] ** 3 / (i.dec[1][0] * i.dec[2][0] ** 2 * i.dec[5][0] ** 4) - 1 / 1.93 > 0:
            return False
        
        if i.dec[4][0] ** 3 / (i.dec[1][0] * i.dec[2][0] * i.dec[6][0] ** 4) - 1 / 1.93 > 0:
            return False
        
        if i.dec[1][0] * i.dec[2][0] - 40 > 0 :
            return False
        
        if i.dec[0][0] / i.dec[1][0] - 12 > 0:
            return False
        
        if 5 - i.dec[0][0] / i.dec[1][0] > 0:
            return False
        
        if 1.9 - i.dec[3][0] + 1.5 * i.dec[5][0] > 0:  
            return False
        
        if 1.9 - i.dec[4][0] + 1.1 * i.dec[6][0] > 0:
            return True
        
        if i.f2() > 1300:
            return False
        
        a = 745 * i.dec[4][0] / (i.dec[1][0] * i.dec[2][0])
        b = 1.575 * 10 ** 8
        if (a ** 2 + b) ** 0.5 / (0.1 * i.dec[6][0] ** 3) > 1100:
            return False
        
        return True

def neighbor(s, c, model):
    sn = deepcopy(s)
    while True:
        sn.dec[c][0] = r.uniform(s.dec[c][1], s.dec[c][2])
        if sn.ok(): 
            break
    return sn

def P(old, new, t):
        return math.exp((old - new) / float(t))

def sa(model):
#     x0 = r.randint(-100000, 100000)
    s0 = model()
    s = deepcopy(s0)
    e = s.getDenormalizedEnergy()  # Initial state, energy.
    sb = deepcopy(s)
    eb = e  # Initial "best" solution
    k = 1  # Energy evaluation count.
    kmax = 1000

    while k < kmax :  # and e > emax While time remains & not good enough:
        if k == 1 or k % 50 == 0: 
            print ("%e" % sb.getDenormalizedEnergy(), end=' ') 
        
        c = r.randint(0, len(s.dec) - 1)
        sn = neighbor(s, c, model)  # Pick some neighbor.
        en = sn.getDenormalizedEnergy()  # Compute its energy.
        if sb.ltOrGt(en, eb):  # Is this a new best?
            sb = deepcopy(sn); eb = en  # Yes, save it.
            print('!', end='')
        elif sb.ltOrGt(en, e):  # Should we jump to better?
            s = deepcopy(sn); e = en  # Yes!
            print('+', end='')
        else :
            if sb.ltOrGt(1, 2):  # Looking for minimum energy?
                e_normalized = abs(float(e - en) / (e + en))
                e_new_normalized_ = 1 - e_normalized
                if P(e_normalized, e_new_normalized_, float(50 * (k / kmax))) < float((r.randint(0, 100)) / 100):  # Should we jump to worse?
                    s = deepcopy(sn); e = en  # Yes, change state.
                    print('?', end='')
                else:
                    print('.', end='')
            else:  # Looking for maximum energy?
                e_normalized = abs(float(en - e) / (e + en))
                e_new_normalized_ = 1 - e_normalized
                if P(e_normalized, e_new_normalized_, float(50 * (k / kmax))) < float((r.randint(0, 100)) / 100):  # Should we jump to worse?
                    s = deepcopy(sn); e = en  # Yes, change state.
                    print('?', end='')
                else:
                    print('.', end='')

        k += 1  # One more evaluation done    
    
        if k % 50 == 0: 
            print ('') 
        
    print ('\nBest Denormalized Energy = ', sb.getDenormalizedEnergy())
    print ('At x = ' , zip(*sb.dec)[0])
    print ('\n\n')

p = 0.5
steps = 10
retries = 50
maxchanges = 20
threshold = 1
evals = 0

def changeRandomInC(c, s, e):
    s_new = deepcopy(s)
    
    s_new.dec[c][0] = r.uniform(s_new.dec[c][1], s_new.dec[c][2])
    ctr = 1000
    while not (s_new.ok()):
        ctr -= 1
        if ctr == 0:
            return s, e
        s_new.dec[c][0] = r.uniform(s_new.dec[c][1], s_new.dec[c][2])
        
    e_best = s_new.getDenormalizedEnergy()
    return s_new, e_best
 
def drange(start, stop, step):
    while start < stop:
            yield start
            start += step
  
def changeCToMaximizeEnergy(c, s, e_old):
    global evals
    step = (s.dec[c][2] - s.dec[c][1]) / float(steps)
    s_new = deepcopy(s)
    s_best = deepcopy(s)
    e_best = e_old
    for i in drange(s.dec[c][1], s.dec[c][2], step):
        evals += 1
        s_new.dec[c][0] = i
        if s_new.ok():
            e_new = s_new.getDenormalizedEnergy()
            if s_new.ltOrGt(e_new, e_best):
                e_best = e_new
                s_best = deepcopy(s_new)
    
    if e_best == e_old:
        return s, e_old  # earlier solution was better.
    return s_best, e_best

def mws(model):
    global evals
    s_best = model()
    e_best = s_best.getDenormalizedEnergy()
    printCtr = 0

    for _ in range(retries) :
        s = deepcopy(s_best)
        s.random()
        e = s.getDenormalizedEnergy()        
        for _ in range(maxchanges) :
            evals += 1
            if printCtr == 0 or printCtr % 50 == 0: 
                print ("%e" % e, end=' ') 
    
#             if e > threshold:
# #                 return x, e
#                 break
            
            # c = random part of solution 
            c = r.randint(0, len(s.dec) - 1)
            if p < float((r.randint(0, 100)) / 100):
                # change a random setting in c
                s_new, e_new = changeRandomInC(c, s, e)
                if s_best.ltOrGt(e_new, e):
                    e = e_new
                    s = deepcopy(s_new)
                    print('?', end='')
                else :
                    print('.', end='')
            else:
                # change setting in c that maximizes score(solution)
                s_new, e_new = changeCToMaximizeEnergy(c, s, e)
                if s_best.ltOrGt(e_new, e):
                    e = e_new
                    s = deepcopy(s_new)
                    print('+', end='')
                else :
                    print('.', end='')
            
            printCtr += 1
            if printCtr % 50 == 0: 
                print ('') 
                
            if s_best.ltOrGt(e, e_best):
                e_best = e
                s_best = deepcopy(s)

    print ('\nBest Denormalized Energy = ', s_best.getDenormalizedEnergy())
    print ('At x = ' , zip(*s_best.dec)[0])
    print ('Evals = ' , evals)            
    print ('\n\n')

"""Global variables for differential evolution algorithm"""
f = 0.75
max = 20
np = 50
cf = 0.3
epsilon = 0.01
# printCtr = 0

"""Generate np candiate soloutions"""   
def getCandiates(model):
    s = model()
    frontier = []
    
    if s.ltOrGt(1, 2):
        e_best = sys.maxint  # goal is to minimize
    else:
        e_best = -1 * sys.maxint
    i_best = -1
    for i in range(np):
        s.random()
        temp = deepcopy(s)
        if temp.ltOrGt(temp.getDenormalizedEnergy(), e_best):
            e_best = temp.getDenormalizedEnergy()
            i_best = i
        frontier.append(temp)
    return i_best, e_best, frontier

def threeOthers(frontier, i):
    while True:
        i2 = r.randint(0, len(frontier) - 1)
        if (i2 != i):
            two = deepcopy(frontier[i2])
            break
        
    while True:
        i3 = r.randint(0, len(frontier) - 1)
        if (i3 != i and i3 != i2):
            three = deepcopy(frontier[i3])
            break

    while True:
        i4 = r.randint(0, len(frontier) - 1)
        if (i4 != i and i4 != i2 and i4 != i3):
            four = deepcopy(frontier[i4])
            break
    
    return two, three, four

def extrapolate(frontier, one, i):
    new = deepcopy(one)

    for _ in range(5):
        two, three, four = threeOthers(frontier, i)
        c = r.randint(0, len(new.dec) - 1)
        for j in range(len(new.dec)):
            if r.random() < cf or j == c:
                new.dec[j][0] = two.dec[j][0] + f * (three.dec[j][0] - four.dec[j][0])
#                 if not ((new.dec[j][0] >= new.dec[j][1]) and (new.dec[j][0] <= new.dec[j][2])):
#                     break
        
        if new.decOk() and new.ok():
            break
        
    if new.decOk() and new.ok():
        return new
    return one

def update(frontier, i_best, e_best):
    total = 0.0
    n = 0
#     for i, x in enumerate(frontier):
    for i in range(len(frontier)):
        x = frontier[i]
        e = x.getDenormalizedEnergy()
        new = extrapolate(frontier, x, i)
        if new.ltOrGt(new.getDenormalizedEnergy(), e_best):
            e_best = new.getDenormalizedEnergy()
            i_best = i
            print('?', end='')
            frontier[i] = new
        elif new.ltOrGt(new.getDenormalizedEnergy(), e):
            frontier[i] = new
            print('+', end='')
        else:
            print('.', end='')
        total += frontier[i].getDenormalizedEnergy()
        n += 1
    return total, n, i_best, e_best


def de(model):
    i_best, e_best, frontier = getCandiates(model)
    for _ in range(max):
        print ("%e" % e_best, end=' ') 
        total, n, i_best, e_best = update(frontier, i_best, e_best)
#         if total / n > (1 - epsilon):            
#             break
        print (' ')
    print ('\nBest Denormalized Energy = ', e_best)
    print ('At x = ' , frontier[i_best])
    print ('\n\n')
    

if __name__ == '__main__':
    for model in [Schaffer, Osyczka2, Kursawe, Golinski]:
        for optimizer in [sa, mws, de]:
            print(optimizer.__name__, " : " , model.__name__)
            optimizer(model)

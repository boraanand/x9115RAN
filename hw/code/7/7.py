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
        return True

    def getobj(i):
        return []

    def ok(i):
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
    
class Kursawe(Model):
     
    def __init__(i):
        i.dec = [[1, -5, 5]]
        i.dec.append([1,-5,5])
        i.dec.append([1,-5,5])
        i.random()
        i.Emin, i.Emax = i.getMinMax()
 
    def normalize(i, e):
 
        if i.Emin > e:
            i.Emin = e
        if i.Emax < e:
            i.Emax = e
 
        return (e - i.Emin) / (i.Emax - i.Emin)

    def f1(i):
        total = 0
        for j in range(len(i.dec)-1):
            e = -0.2 * sqrt(i.dec[j][0]**2 + i.dec[j+1][0]**2)
            total+= -10*exp(e)
        return total
    
    def f2(i):
        total = 0
        for j in range(len(i.dec)):
            total+= abs(i.dec[j][0])**0.8 + 5*sin(i.dec[j][0]**3)
        return total
         
    def objs(i):
        return [i.f1(), i.f2()]
     
    def getEnergy(i):
        return i.normalize(sum(i.objs()))
 
    def getDenormalizedEnergy(i):
        return sum(i.objs())

class Schaffer(Model):
    
    def __init__(i):
        i.dec = [ [1, -10 ** 2, 10 ** 2] ]
        i.random()
        i.Emin, i.Emax = i.getMinMax()

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
    
    def getEnergy(i):
        return i.normalize(sum(i.objs()))

    def getDenormalizedEnergy(i):
        return sum(i.objs())

class Osyczka2(Model):
    def __init__(i):
        i.dec = [[-1, 0, 10]]
        i.dec.append([-1,0,10])
        i.dec.append([-2,1,5])
        i.dec.append([-1,0,6])
        i.dec.append([-2,1,5])
        i.dec.append([-1,0,10])
        i.random()
        i.Emin, i.Emax = i.getMinMax()

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


    # less than. Goal is to minimize. Return true if new < best.
    def ltOrGt(i, Enew, Ebest):
        if Enew > Ebest:
            return True
        return False
        
    def objs(i):
        f1 = -1 * (25*(i.dec[0][0]-2) ** 2 + (i.dec[1][0] - 2) ** 2 + (i.dec[2][0] - 1) ** 2 * (i.dec[3][0] - 4) ** 2 + (i.dec[4][0] - 1) ** 2)
        f2 = i.dec[0][0] ** 2 + i.dec[1][0] ** 2 + i.dec[2][0] ** 2 + i.dec[3][0] ** 2 + i.dec[4][0] ** 2 + i.dec[5][0] ** 2
        return [f1, f2]
    
    def getEnergy(i):
        return i.normalize(sum(i.objs()))
    
    def getDenormalizedEnergy(i):
        return sum(i.objs())

def neighbor(s, c, model):
    sn = deepcopy(s)
    while True:
        sn.dec[c][0] = r.uniform(s.dec[c][1], s.dec[c][2])
        if sn.ok(): 
            break
    return sn

def P(old, new, t):
        return math.exp(float(old - new) / float(t))

def sa(model):
#     x0 = r.randint(-100000, 100000)
    s0 = model()
    s = deepcopy(s0)
    e = s.getEnergy()  # Initial state, energy.
    sb = deepcopy(s)
    eb = e  # Initial "best" solution
    k = 1  # Energy evaluation count.
    kmax = 1000

    while k < kmax :  # and e > emax While time remains & not good enough:
        if k == 1 or k % 50 == 0: 
            print ("%e" % sb.getEnergy(), end=' ') 
        
        c = r.randint(0, len(s.dec) - 1)
        sn = neighbor(s, c, model)  # Pick some neighbor.
        en = sn.getEnergy()  # Compute its energy.
        if sb.ltOrGt(en,eb): #Is this a new best?
            sb = deepcopy(sn); eb = en  # Yes, save it.
            print('!', end='')
        elif sb.ltOrGt(en,e): #Should we jump to better?
            s = deepcopy(sn); e = en  # Yes!
            print('+', end='')
        else :
            if sb.ltOrGt(1,2): #Looking for minimum energy?
                if P(e, en, float(50 * (k / kmax))) < float((r.randint(0, 100)) / 100):  # Should we jump to worse?
                    s = deepcopy(sn); e = en  # Yes, change state.
                    print('?', end='')
                else:
                    print('.', end='')
            else: #Looking for maximum energy?
                if P(1-e, 1-en, float(50 * (k / kmax))) < float((r.randint(0, 100)) / 100):  # Should we jump to worse?
                    s = deepcopy(sn); e = en  # Yes, change state.
                    print('?', end='')
                else:
                    print('.', end='')

        k += 1  # One more evaluation done    
    
        if k % 50 == 0: 
            print ('') 
        
    print ('\nBest energy = ', eb)
    print ('Best Denormalized Energy = ', sb.getDenormalizedEnergy())
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
        
    e_best = s_new.getEnergy()
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
            e_new = s_new.getEnergy()
            if s_new.ltOrGt(e_new, e_best):
                e_best = e_new
                s_best = deepcopy(s_new)
    
    if e_best == e_old:
        return s, e_old  # earlier solution was better.
    return s_best, e_best

def mws(model):
    global evals
    s_best = model()
    e_best = s_best.getEnergy()
    printCtr = 0

    for _ in range(retries) :
        s = deepcopy(s_best)
        s.random()
        e = s.getEnergy()        
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

    print ('\nBest energy = ', e_best)
    print ('Best Denormalized Energy = ', s_best.getDenormalizedEnergy())
    print ('At x = ' , zip(*s_best.dec)[0])
    print ('Evals = ' , evals)            
    print ('\n\n')

"""Global variables for differential evolution algorithm"""
f = 0.75
max = 100
np = 100
cf = 0.3
epsilon = 0.01

"""Generate np candiate soloutions"""

def extraploate(frontier,one):
    
def getCandiates(model):
    s = model()
    frontier = []
    for _ in range(np):
	s.random()
        temp = deepcopy(s)
	frontier.append(temp)
    return frontier

def update(frontier):
    total = 0.0
    n = 0
    for i,x in enumerate(frontier):
	e = x.getEnergy()
	new = extrapolate(frontier,x)
	if new.getEnergy() > e:
	    frontier[i] = new
    	total += frontier[i].getEnergy()
	n += 1
    return total,n

def de(model):
    frontier =  getCandiates(model)
    for k in range(max):
	total,n = update(frontier)
    if total/n > (1 - epsilon):
	break
    print frontier     # printing frontier


if __name__ == '__main__':
    for model in [Osyczka2]:
        for optimizer in [de]:
            print(optimizer.__name__, " : " , model.__name__)
            optimizer(model)

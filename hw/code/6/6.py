from __future__ import print_function, division
import random as r
import math
import copy
from copy import deepcopy

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

    def ltOrGt(i):
        return True
    

class Schaffer(Model):
    
    def __init__(i):
        i.dec = [ [1, -10 ** 5, 10 ** 5] ]
        i.random()
        i.Emin = 2
        i.Emax = 20000400004

    def normalize(i, e):

        if i.Emin > e:
            i.Emin = e
        if i.Emax < e:
            i.Emax = e

        return (e - i.Emin) / (i.Emax - i.Emin)


    # less than. Goal is to minimize. Return true if new < best.
    def ltOrGt(i, Enew, Ebest):
        if Enew < Ebest:
            return True
        return False
        
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
        i.dec = [[1, 0, 10]]
	i.dec.append([1,0,10])
	i.dec.append([2,1,5])
	i.dec.append([1,0,6])
	i.dec.append([2,1,5])
	i.dec.append([1,0,10])
        i.random()
        i.Emin = -396.221369935
        i.Emax = 146.314249947

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
        while not i.okx1x2():
            i.dec[0][0] = r.uniform(i.dec[0][1], i.dec[0][2])
            i.dec[1][0] = r.uniform(i.dec[1][1], i.dec[1][2])
        while not i.okx3x4():
            i.dec[2][0] = r.uniform(i.dec[2][1], i.dec[2][2])
            i.dec[3][0] = r.uniform(i.dec[3][1], i.dec[3][2])
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
        
    print ('\nBest Energy = ', eb, ' at x = ', zip(*sb.dec)[0])
    print ('\nBest Denormalized Energy = ', sb.getDenormalizedEnergy(), ' at x = ', zip(*sb.dec)[0])
    print ('\n')

if __name__ == '__main__':
    for model in [Schaffer,Osyczka2]:
        for optimizer in [sa]:
#             print(optimizer.__name__, +" : " + model.__name__)
            optimizer(model)

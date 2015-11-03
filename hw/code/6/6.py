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

#     def clone(i, other):
#         i.dec = other.dec[:]

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
    
# randomNu = r.randint(-100000, 2 * i.x - (-100000))  # Select neighbour a random in in a radius from current x to min.

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
#         global Emin
#         Emin = min(Emin, en)
        if en < eb:  # Is this a new best?
            sb = deepcopy(sn); eb = en  # Yes, save it.
            print('!', end='')
        elif en < e:  # Should we jump to better?
            s = deepcopy(sn); e = en  # Yes!
            print('+', end='')
        elif P(e, en, float(50 * (k / kmax))) < float((r.randint(0, 100)) / 100):  # Should we jump to worse?
            s = deepcopy(sn); e = en  # Yes, change state.
            print('?', end='')
        else:
            print('.', end='')
        k += 1  # One more evaluation done    
    
        if k % 50 == 0: 
            print ('') 
    print ('\nBest Energy = ', eb, ' at x = ', sb.dec[0][0])

if __name__ == '__main__':
    for model in [Schaffer]:
        for optimizer in [sa]:
#             print(optimizer.__name__, +" : " + model.__name__)
            optimizer(model)

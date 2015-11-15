from __future__ import print_function, division
import random as r
from copy import deepcopy
from math import exp
from Models import *

def neighbor(s, c, model):
    sn = deepcopy(s)
    while True:
        sn.dec[c][0] = r.uniform(s.dec[c][1], s.dec[c][2])
        if sn.ok():
            break
    return sn

def P(old, new, t):
        return exp(float(old - new) / float(t))

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

if __name__ == '__main__':
    for model in [Schaffer, Osyczka2, Kursawe]:
        for optimizer in [sa, mws]:
            print(optimizer.__name__, " : " , model.__name__)
            optimizer(model)

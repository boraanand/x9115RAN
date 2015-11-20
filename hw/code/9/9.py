from __future__ import print_function, division
import random as r
import math
from copy import deepcopy
import sys
from math import sqrt, exp, sin
#from sk import *

class Model(object):
    def random(i):
        while True:
            for j in range(len(i.dec)):
                i.dec[j][0] = r.uniform(i.dec[j][1], i.dec[j][2])
            if i.ok():
                break

    def __init__(i):
        i.dec = [[0, 0, 0]]  # [0][0] has dec name (example x1), [0][1] it's low, [0][2] it's high

    def getEnergy(i):
        return i.normalize(sum(i.objs()))

    def getDenormalizedEnergy(i):
        return sum(i.objs())

    def objs(i):
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


class DTLZ_7(Model):
    n = 10 # Number of decisions
    M = 2  # Number of obectives

    def __init__(i):
        i.dec =[[-1, 0 ,1]]
        for x in range((i.n - 1)):
            i.dec.append([-1, 0, 1])
        i.random()

    def h1(i,g):
        summation = 0.0
        for j in range(i.M - 1):
            f_i = i.dec[j][0]
            summation += f_i() / (1 + g) * (1 + math.sin(3 * math.pi * f_i()))
        return (i.M - summation)

    def f1(i):
        return i.dec[0][0]

    def f2(i):
        g = 1 + 9.0/len(i.dec) * sum(x[0] for x in i.dec)
        summation = 0.0
        for j in range(i.M - 1):
            f_i = i.dec[j][0]
            summation += (f_i / (1 + g)) * (1 + math.sin(3 * math.pi * f_i))
        h =  (i.M - summation)
        b = (1 + g) * h
        return b

    def objs(i):
        return [i.f1(), i.f2()]


def neighbor(s, c, model):
    sn = deepcopy(s)
    while True:
        sn.dec[c][0] = r.uniform(s.dec[c][1], s.dec[c][2])
        if sn.ok():
            break
    return sn

def P(old, new, t):
    #print ('math exp ',(old-new)/float(t))
    try:
       return math.exp((old - new) / float(t))
    except:
       return 1

def sa(model):
#     x0 = r.randint(-100000, 100000)
    s0 = model()
    s = deepcopy(s0)
    e = s.getDenormalizedEnergy()  # Initial state, energy.
    sb = deepcopy(s)
    eb = e  # Initial "best" solution
    k = 1  # Energy evaluation count.
    kmax = 1000
    era_prev = [-1,-1]
    era_cur = []
    era_cur.append(e)
    while k < kmax :  # and e > emax While time remains & not good enough:
        if k == 1 or k % 50 == 0:
            print ("%e" % sb.getDenormalizedEnergy(), end=' ')

        c = r.randint(0, len(s.dec) - 1)
        sn = neighbor(s, c, model)  # Pick some neighbor.
        en = sn.getDenormalizedEnergy()  # Compute its energy.
        era_cur.append(en) #Store energy in current era list.
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
            if different(era_prev,era_cur):
               era_prev = deepcopy(era_cur)
               era_cur = []
            else:
               print ('Early Termination in era : ',k/50)
               break;

    print ('\nBest Denormalized Energy = ', sb.getDenormalizedEnergy())
    print ('At x = ' , zip(*sb.dec)[0])
    print ('\n\n')
    return sb

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
    isFlag = 0
    s_best = model()
    e_best = s_best.getDenormalizedEnergy()
    printCtr = 0
    era_prev = [-1, -1]
    era_cur = []
    #era_cur.append(e_best)
    for _ in range(retries) :
        s = deepcopy(s_best)
        s.random()
        e = s.getDenormalizedEnergy()
        #era_cur.append(e) #Store energy in current era list.
        for _ in range(maxchanges) :
            evals += 1
            if printCtr == 0 or printCtr % 50 == 0:
                print ("%e" % e_best, end=' ')

            c = r.randint(0, len(s.dec) - 1)
            if p < float((r.randint(0, 100)) / 100):
                # change a random setting in c
                s_new, e_new = changeRandomInC(c, s, e)
                era_cur.append(e_new) #Store energy in current era list.
                if s_best.ltOrGt(e_new, e):
                    e = e_new
                    s = deepcopy(s_new)
                    print('?', end='')
                else :
                    print('.', end='')
            else:
                # change setting in c that maximizes score(solution)
                s_new, e_new = changeCToMaximizeEnergy(c, s, e)
                era_cur.append(e_new) #Store energy in current era list.
                if s_best.ltOrGt(e_new, e):
                    e = e_new
                    s = deepcopy(s_new)
                    print('+', end='')
                else :
                    print('.', end='')

            printCtr += 1
            if printCtr % 50 == 0:
                print ('')
                if different(era_prev,era_cur):
                   era_prev = deepcopy(era_cur)
                   era_cur = []
                else:
               	   print ('Early Termination in era : ',printCtr/50)
                   isFlag = 1
                   break
            if isFlag:
                break;
            if s_best.ltOrGt(e, e_best):
                e_best = e
                s_best = deepcopy(s)


    print ('\nBest Denormalized Energy = ', s_best.getDenormalizedEnergy())
    print ('At x = ' , zip(*s_best.dec)[0])
    print ('Evals = ' , evals)
    print ('\n\n')
    return s_best

"""Global variables for differential evolution algorithm"""
f = 0.75
max = 20
np = 50
cf = 0.3
epsilon = 0.01
# printCtr = 0
era_cur = []
era_prev = [-1, -1]

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

        if new.decOk() and new.ok():
            break

    if new.decOk() and new.ok():
        return new
    return one

def update(frontier, i_best, e_best):
    global era_cur, era_prev
    total = 0.0
    n = 0
    for i in range(len(frontier)):
        x = frontier[i]
        e = x.getDenormalizedEnergy()
        new = extrapolate(frontier, x, i)
        era_cur.append(new.getDenormalizedEnergy())
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
    global era_cur, era_prev, np
    np = 50
    i_best, e_best, frontier = getCandiates(model)
    for j in range(max):
        print ("%e" % e_best, end=' ')
        total, n, i_best, e_best = update(frontier, i_best, e_best)
#         if total / n > (1 - epsilon):
#             break
        print (' ')
        if different(era_prev,era_cur):
            era_prev = deepcopy(era_cur)
            era_cur = []
        else:
       	    print ('Early Termination in era : ',j+1)
            break

    print ('\nBest Denormalized Energy = ', e_best)
    print ('At x = ' , frontier[i_best])
    print ('\n\n')
    return frontier[i_best]



def ga(model):
    global era_cur, era_prev, np
    np = 100
    i_best, e_best, frontier = getCandiates(model)
    no_of_generation = 1000

    for i in range(no_of_generation):
        if i % 100 == 0:
            print('\n')

        papa_pos, mama_pos = select(frontier)
        papa = frontier[ papa_pos ]
        mama = frontier[ mama_pos ]
        mutate([papa, mama])
        new_can = crossover([papa, mama])

        e_new = new_can.getDenormalizedEnergy()
        e_papa = papa.getDenormalizedEnergy()
        e_mama = mama.getDenormalizedEnergy()

        if e_new < e_best:
            i_best = np - 1
            e_best = new_can.getDenormalizedEnergy()
            print('+', end = '')
        else:
            print('.', end='')

        # TODO : should we replace the parents??
        # frontier.append(new_can)
        energies = [(e_new, np), (e_papa, papa_pos), (e_mama, mama_pos)]

        if e_new < e_papa and e_new < e_mama:
            if e_papa > e_mama:
                frontier[papa_pos] = new_can
            else:
                frontier[mama_pos] = new_can
        elif e_new < e_papa:
            frontier[papa_pos] = new_can
        elif e_new < e_mama:
            frontier[mama_pos] = new_can


def select(frontier):
    # TODO: How to select and how many to select?? Not clear about binary domination thing
    a = r.randint(0, len(frontier)-1)
    while True:
        b = r.randint(0, len(frontier)-1)
        if b != a: break
    return (a, b)

def mutate(parents, mutate_prob = 0.05):
    # TODO: Any specific mutation method ??
    for individual in parents:
        if r.random() < mutate_prob:
            pos = r.randint(0, len(individual.dec)-1)
            individual.dec[pos][0] = r.randint( individual.dec[pos][1], individual.dec[pos][1] )

def crossover(parents, mutate_prob = 0.05):
    # TODO: What if more than 2 parents ??
    pos = r.randint(0, len(parents[0].dec)-1)
    can = deepcopy(parents[0])
    can.dec[pos:] = parents[1].dec[pos:]
    return can




if __name__ == '__main__':
  for model in [DTLZ_7]:
    #rdiv = [['sa'],['mws'],['de']]

    for optimizer in [ga]:
        optimizer(model)
            #rdiv[k].append(en)
    #rdivDemo(rdiv)
    print ("\n\n")

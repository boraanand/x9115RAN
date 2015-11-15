import random as r
from math import sqrt, exp, sin
import sys

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
        print(min , " : " , max)
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

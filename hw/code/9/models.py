from copy import deepcopy
import random as r
from util import *
import math

class Decision():
    """ A wrapper class on decisions """
    def __init__(i, name, low, high):
        i.name = name
        i.low = low
        i.high = high


class Objective():
    """ A wrapper class on Objectives """
    def __init__(i, name, function, better=lt):
        i.name = str(name)
        i.function = function
        i.better = better

class Candidate(object):
    "A candidate decision values, objective scores, and energy"
    def __init__(self, decs = [], objs_score = [], energy = None):
        self.decs = decs
        self.objs_score = objs_score
        self.energy = energy

    def clone(self):
        new_can = Candidate()
        new_can.decs = deepcopy(self.decs)
        new_can.objs_score = self.objs_score[:]
        new_can.energy = self.energy
        return new_can

class Model(object):

    def __init__(i):
        i.decs = []
        i.objs = []

    def get_objs(i):
        return []

    def ok(i, can):
        return True

    def energy(i, can):
        can.objs_score = [obj.function(can) for obj in i.objs]
        return sum(can.objs_score)

    def __repr__(i):
        return str(zip(*i.decs)[0])

    def generate(i):
        """ Generates a candidate """
        count = 0
        while True:
            decs = [r.uniform(d.low, d.high) for d in i.decs]
            one = Candidate(decs = decs)
            status = i.ok(one)
            count += 1
            if status:
                return one

    def dominates(i, can_1, can_2, better=lt):
        """
        Static method to check if one candidate dominates the other.
        :param can_1: List of points A
        :param can_2: List of points B
        :param better: greater/lesser function that used for domination
        """
        at_least = False

        can_1.objs_score = [obj.function(can_1) for obj in i.objs]
        can_2.objs_score = [obj.function(can_2) for obj in i.objs]

        for a, b in zip(can_1.objs_score, can_2.objs_score):
          if better(a,b):
            at_least = True
          elif a == b:
            continue
          else:
            return False
        return at_least

class DTLZ_1(Model):
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.objs = []
        self.decs = []


class DTLZ_3(Model):
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.objs = []
        self.decs = []

class DTLZ_5(Model):
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.objs = []
        self.decs = []

class DTLZ_7(Model):
    def __init__(i, n=10, m=2):
        """
            Args:
                n = number of decisions
                m = number of objectives
        """
        i.n = n
        i.m = m       
        i.decs = [Decision(name=d, low=0, high=1) for d in range(i.n)]
        i.objs = i.get_objs()

    def get_objs(i):
        # first m-1 objectives are same as respective decisions
        objectives = []
        for j in range(i.m - 1):
            def f(can):
                return can.decs[0]
            objectives.append(Objective(name = j, function = f))

        def fm(can):
            g = 1 + 9.0 / len(can.decs) * sum(can.decs)
            summation = 0.0
            for j in range(i.m - 1):
                f_i = can.decs[j]
                summation += (f_i / (1 + g)) * (1 + math.sin(3 * math.pi * f_i))
            h = (i.m - summation)
            return (1 + g) * h

        objectives.append(Objective(name = i.m-1, function = fm))
        return objectives[:]
from __future__ import math
from gadgets import Candidate, About
import math

Decision = Objective = About

class DTLZ_7(Candidate):
    n = 10 # Number of decisions
    M = 2  # Number of obectives
    self.objs = []
    self.decs = []

    def about(self):
        def dec(x):
            return Decision(x, lo=0, hi=1)

        self.decs = [dec(x) for x in range(DTLZ.n)]

        def h( objs, g):
            summation = 0.0
            for i in range(DTLZ_7.M - 1):
                f_i = self.decs[i].maker
                summation += f_i() / (1 + g) * (1 + math.sin(3 * math.pi * f_i()))
            return (DTLZ_7.M - summation)

        def f1(can):
            return can.decs[0]

        def f2(can):
            g = 1 + 9.0/len(can.decs) * sum(x for x in can.decs)
            b = (1 + g) * h(can.objs[:-1], g)

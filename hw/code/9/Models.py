from gadgets import Candidate, About
Decision = Objective = About

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

class DTLZ_7(Moel):
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.objs = []
        self.decs = []

    def about(self):
        def dec(x):
            return Decision(x, lo=0, hi=1)

        self.decs = [dec(x) for x in range(self.n)]

        def h( objs, g):
            summation = 0.0
            for i in range(self.m - 1):
                f_i = self.decs[i].maker
                summation += f_i() / (1 + g) * (1 + math.sin(3 * math.pi * f_i()))
            return (self.m - summation)

        def f1(can):
            return can.decs[0]

        def f2(can):
            g = 1 + 9.0/len(can.decs) * sum(x for x in can.decs)
            b = (1 + g) * h(can.objs[:-1], g)

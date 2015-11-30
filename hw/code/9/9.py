from __future__ import print_function, division
from models import *
from algorithms import *

if __name__ == '__main__':
    for model in [DTLZ_5, DTLZ_7]:
        for optimizer in [ga]:
            optimizer().optimize(model())
        print ("\n\n")
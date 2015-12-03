from __future__ import print_function, division
from ..source.models import *
from ..source.algorithms import *

if __name__ == '__main__':
   
    for model in [DTLZ_3, DTLZ_1, DTLZ_3, DTLZ_5]:
        for optimizer in [ga]:
            optimizer().optimize(model(n=10, m=2))
        print ("\n\n")

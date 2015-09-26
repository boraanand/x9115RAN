from __future__ import print_function, division
import random as r
import math

Emin = 3044
Emax = 19993600514

class Schaffer():
    def __init__(i, x): 
        i.x = x

    def f1(i): return i.x ** 2
  
    def f2(i): return (i.x - 2) ** 2

    def E(i):
        return (i.f1() + i.f2() - Emin) / (Emax - Emin)

    def neighbor(i):  
        randomNu = r.randint(-100000, 2 * i.x - (-100000))
        return Schaffer(randomNu)

def P(old, new, t):
    return math.exp((old - new) / t)

def sa(x0):
    s0 = Schaffer(x0)
    s = s0; e = s.E()  # Initial state, energy.
    sb = s; eb = e  # Initial "best" solution
    k = 1  # Energy evaluation count.
    kmax = 1000
    emax = -2.0

    while k < kmax :  # and e > emax While time remains & not good enough:
        sn = s.neighbor()  # Pick some neighbor.
        en = sn.E()  # Compute its energy.
#         global Emin
#         Emin = min(Emin, en)
        if en < eb:  # Is this a new best?
            sb = sn; eb = en  # Yes, save it.
            print('!', end='')

        if en < e:  # Should we jump to better?
            s = sn; e = en  # Yes!
            print('+', end='')
        elif P(e, en, float(1 - (k / kmax))) < float((r.randint(0, 100)) / 100):  # Should we jump to worse?
            s = sn; e = en  # Yes, change state.
            print('?', end='')
    
        print('.', end='')
        k += 1  # One more evaluation done    
    
        if k % 50 == 0: 
            print (sb.E(), sb.x) 
#           print("\n")
  
    return sb

if __name__ == '__main__':
    sa(r.randint(-100000, 100000))

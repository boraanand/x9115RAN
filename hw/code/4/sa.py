from __future__ import print_function, division
import random as r

class Schaffer():
  def __init__(i, x, min_, max_): 
    i.x = x
    i.min_ = min_
    i.max_ = max_
  
  def f1(i): return i.x**2
  
  def f2(i): return (i.x-2)**2

  def E(i):
    return (f1() + f2() - i.min_)/ (i.max_ - i.min_)

  def neighbor(i):
    return r.randrange(i.min_, i.max_)

def P(old,new,t):
  return e**((old-new)/t)

def sa(x0, min_, max_):
  s0 = Schaffer(x0, min_, max_)
  s = s0; e = s.E()                 # Initial state, energy.
  sb = s; eb = e                    # Initial "best" solution
  k = 0                             # Energy evaluation count.

  while k < kmax and e > emax:      # While time remains & not good enough:
    sn = s.neighbor()               # Pick some neighbor.
    en = sn.E()                     # Compute its energy.
    if en < eb:                     # Is this a new best?
      sb = sn; eb = en              # Yes, save it.
      print('!', end='')

    if en < e:                      # Should we jump to better?
      s = sn; e = en                # Yes!
      print('+', end = '')
    elif P(e, en, k/kmax) < rand(): # Should we jump to worse?
      s = sn; e = en                # Yes, change state.
      print('?', end='')
    
    print('.', end='')
    k +=  1                         # One more evaluation done    
    
    if k % 50 == 0: print("\n",sb)
  
  return sb
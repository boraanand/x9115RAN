from __future__ import print_function, division

def sa(s0):
  s = s0[:]; e = E(s)                  # Initial state, energy.
  sb = s; eb = e                    # Initial "best" solution
  k = 0                              # Energy evaluation count.
  while k < kmax and e > emax:         # While time remains & not good enough:
    sn = neighbor(s)                 #   Pick some neighbor.
    en = E(sn)                       #   Compute its energy.
    if en < eb:                     #   Is this a new best?
      sb = sn; eb = en          #     Yes, save it.
      print('!', end='')

    if en < e:                   # Should we jump to better?
      s = sn; e = en            #    Yes!
      print('+', end = '')
    elif P(e, en, k/kmax) < rand(): # Should we jump to worse?
      s = sn; e = en            #    Yes, change state.
      print('?', end='')
    
    print('.', end='')
    k +=  1                        #   One more evaluation done    
    
    if k % 50 == 0: print("\n",sb)
  
  return sb
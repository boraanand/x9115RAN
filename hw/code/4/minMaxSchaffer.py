import random as r

def f1(x): return x ** 2

def f2(x): return (x - 2) ** 2

if __name__ == '__main__':
    min = 100000
    max = -100000
    
    for _ in range(5000000):
        x = r.randint(-100000, 100000)
        e = f1(x) + f2(x)
        if min > e:
            min = e
        if max < e:
            max = e
        
    
    print 'Emin: ', min
    print 'Emax: ', max
    
# Output #
# Emin:  3044
# Emax:  19993600514

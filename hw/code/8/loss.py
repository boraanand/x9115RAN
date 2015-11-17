import math

def loss1(i,x,y):
    return (x - y) #if better(i) == lt else (y - x)

def expLoss(i,x,y,n):
    return math.exp( loss1(i,x,y) / n)

def loss():
    x = [1,2]
    y = [1,4]
    n      = min(len(x), len(y)) #lengths should be equal 
    losses = [ expLoss(i,xi,yi,n)
                 for i, (xi, yi) 
                   in enumerate(zip(x,y)) ]
    return sum(losses) / n

print loss()

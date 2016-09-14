import math

def dist(x,y):
    n = len(x)
    if n != len(y):
        raise TypeError('Different number of arguments')
    d = 0
    for i in range(n):
        d+=(x[i]-y[i])**2
    return math.sqrt(d)

import numpy as np
import math


def FirstTask():
    start = 0
    end = 2
    step = 0.2
    eps = 0.000001

    x = np.arange(start, end + step, step)
    n=0
    S = x.copy()
    a = x.copy()
    q = np.zeros(len(x))


    while(max(abs(a))>eps):
        for i in range(len(q)):
            q[i] = -((x[i]**2)*(2*n + 1))/((2*n + 3)*(n+1))
            tmp  = q[i] * a[i]
            S[i] = S[i] + tmp
            a[i] = tmp
        n+=1
    S=S*2/math.sqrt(math.pi)
    for i in range(len(x)):
        print('f({}) = {}'.format(round(x[i],2),round(S[i],6)))
    return x,S

def FirstTaskWithParametrs(x,eps):

    n=0
    S = x.copy()
    a = x.copy()
    q = np.zeros(len(x))


    while(max(abs(a))>eps):
        for i in range(len(q)):
            q[i] = -((x[i]**2)*(2*n + 1))/((2*n + 3)*(n+1))
            tmp  = q[i] * a[i]
            S[i] = S[i] + tmp
            a[i] = tmp
        n+=1
    S=S*2/math.sqrt(math.pi)
    # for i in range(len(x)):
    #     print('f({}) = {}'.format(round(x[i],2),round(S[i],6)))
    return S
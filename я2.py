from Tabulirovanie_transtsendentnykh_funktsiy import *
import matplotlib.pyplot as plt

from scipy.special import *
from scipy.integrate import quad

def SecondTask(count):
    n = count
    print('Всего точек узловых = {}'.format(n))
    
    x = np.linspace(0, 2, n)
    f = np.array(FirstTaskWithParametrs(x, 0.000001))
    print ('Узловые точки и f(x)')
    for i in range(len(x)):
        print('f({:.3f})={:.6f}' .format( x[i], f[i]))
    xMiddle = [x[i] + (x[i] - x[i - 1]) / 2 for i in range(1, len(x) - 1)]
    xMiddle.insert(0, 0)
    xMiddle = np.array(xMiddle)
    fInMiddle = np.array(FirstTaskWithParametrs(xMiddle, 0.000001))
    print('Серединные точки и f(x)')
    for i in range(len(xMiddle)):
        print('f({:.3f})={:.6f}'.format(xMiddle[i], fInMiddle[i]))
    nMiddle=len(xMiddle)
    print('Всего точек узловых = {}'.format(nMiddle))

    def Ln(currentX):
        S=0
        for i in range(n):
            proiz=1
            for j in range(n):
                if i!=j:
                    proiz*=(currentX-x[j])/(x[i]-x[j])
            S+=proiz*f[i]
        return S
    L=np.array([Ln(xi) for xi in xMiddle])
    difference = abs(fInMiddle - L)
    print('Максимальное значение погрешности интерполирования = {}'.format(max(difference)))
    return x, f, L, difference

import scipy.integrate as integrate;
import numpy as np
from math import cos
import scipy
 # нужно сделать эксперимент Если квадратурная формула формула нужно вычислить погрешность и разделить на h
#вычислить найти макс разность разделить она должна стремиться к const

def task3(N):
    print('Количество точек для разбиения отрезка интегрирования [0,2] = {}'.format(N))
    xVector = np.linspace(0,2,15)
    integrals = [scipy.special.erf(x) for x in xVector]
    quadrature = []
    error=[]
    for i in range(15):
        z = np.linspace(0,2,N)
        hn = xVector[i]/N
        S = 0
        for j in range(1,N):
            S+=hn*(np.exp(-z[j-1]*z[j-1]) + 4 * np.exp(-((z[j]+z[j-1])/2)**2) + np.exp(-z[j]*z[j]))/6
        S = S*2/np.pi
        quadrature.append(S)
        error.append(abs(S-integrals[i]))

    quadrature=np.array(quadrature)
    print('   Точки x       Интеграл(идеал)   Квадратурные     Разница')

    for i in range(15):
        print('{0:10.2f}'.format(xVector[i]),end=' ')
        print('{0:15.5f}'.format(integrals[i]), end=' ')
        print('{0:15.5f}'.format(quadrature[i]), end=' ')
        print('{0:15.5f}'.format(error[i]), end=' ')
        print()
    return error


errorsList=[]
for i in range(5,40):
    errorsList.append(max(task3(i))/i)
import matplotlib.pyplot as plt

plt.plot(np.arange(5,40), errorsList)
plt.show()

import scipy.integrate as integrate;
import numpy as np
from math import cos
import scipy
 # нужно сделать эксперимент Если квадратурная формула формула нужно вычислить погрешность и разделить на h
#вычислить найти макс разность разделить она должна стремиться к const


#print(f'результат: {что угодно преобразует к строке }')
# mask = 'результат {} из числа {}'
# print(строка.format())

def task3(start,end):
    integralConst = scipy.special.erf(2)
    integral = np.array([integralConst for i in range(start,end)])
    quadrature = []
    error=[]
    for i in range(start,end):
        print('Количество точек для разбиения отрезка интегрирования [0,2] = {}'.format(i))
        z = np.linspace(0,2,i)
        hn = 2/i
        S = 0
        for j in range(1,i):
            S+=hn*(np.exp(-z[j-1]*z[j-1]) + 4 * np.exp(((z[j]+z[j-1])/2)**2) + np.exp(-z[j]*z[j]))/6
        S = S*2/np.pi
        quadrature.append(S)
        error.append(abs(S-integralConst)/i**2)

    print('   Точки x       Интеграл(идеал)   Квадратурные     Разница')
    for i in range(end-start):
        print('{0:10.2f}'.format(2),end=' ')
        print('{0:15.5f}'.format(integral[i]), end=' ')
        print('{0:15.5f}'.format(quadrature[i]), end=' ')
        print('{0:15.5f}'.format(error[i]), end=' ')
        print()
    return error

import matplotlib.pyplot as plt

plt.plot(np.arange(10,1000), task3(10,1000))
plt.show()

# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Nandini Bhosale\.spyder2\.temp.py
"""

import numpy
from matplotlib import pyplot as plt
from numpy import exp
import scipy,scipy.optimize
from numpy import array
import scipy
from scipy import exp
from scipy.optimize import fmin,fsolve
from scipy import array

k=1.64*10**-2
tao=1.2 #tao is Q/V

x=array([0,0.1,0.4,0.9,1.8,5.5,6,7,8,9,7.5,4.5])
y=array([ 0.499,0.476,0.413,0.327,0.214,0.038,0.03,0.019,0.012,0.007,0.015,0.06])

def error(p):
    err=(y-p[0]*exp(-p[1]*x))**2
    err=sum(err)
    return err

p=fmin(error,[0.5,-0.5])
print p



def solve(n):
    a=p[1]-n[0]/n[1]*tao-k
    b=p[0]-n[0]/n[1]*tao-k*(1-n[0])
    return [a,b]
    
v=fsolve(solve,[0.234,.57])
print '   n       m '
print v


k=1.64*10**-2
n=v[0]
m=v[1]
tao=1.2

t=numpy.linspace(0,20,101)
A1=(n/m*tao+k*(1-n))/(n/m*tao+k)*(1-exp((-n/m*tao+k)*t[100]))
A2=(tao)/(tao+k)*(1-exp((-tao+k)*t[100]))

C=(n/m*tao+k*(1-n))*exp((-n/m*tao+k)*t)
Co=tao*exp(-t*(tao+k))
plt.plot(t,Co)
plt.plot(t,C)
plt.show()

print ''
print '      A1             A2'
print A1, A2


    

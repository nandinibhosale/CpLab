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

#data fit to get A and B of A*e^Bx
def error(p):
    err=(y-p[0]*exp(-p[1]*x))**2
    err=sum(err)
    return err

p=fmin(error,[0.5,-0.5])
print p


#solving to get n=bypass fraction ,m=deadvolume fraction
def solve(n):
    a=p[1]-n[0]/n[1]*tao-k
    b=p[0]-n[0]/n[1]*tao-k*(1-n[0])
    return [a,b]
    
v=fsolve(solve,[0.234,.57])
print '   n       m '
print v

#using n amd m obtained for given data,plot C vs time for nonideal and compare with ideal
k=1.64*10**-2
n=v[0]
m=v[1]
tao=1.2

t=numpy.linspace(0,20,101)
#Area under curve for ideal and nonideal will be same since it is amount of tracer/reactant
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

#ideal isothermal cstr PI control
    
from scipy import linspace,exp
from scipy.optimize import fsolve
from scipy.integrate import odeint,trapz
import random
from pylab import plot,show,subplot,figure

Fis=2.0
Cais=2.0
k0=0.2
E=10.0
R=8.314

Tis=100.0
J=2.0
p=1000.0
Cp=4.0
Qc=1.0
A=0.1
Re=0.5

Kc1=50.0
Kc2=20000.0

TTi1=0.1
TTi2=0.001



#to calculate steady state values
def steady(x):
    h=x[0]
    Ca=x[1]
    F=h/Re
    T=x[2]
    e1=(Fi-F)/A#dF/dt
    e2=Fi/A/h*(Cai-Ca)-k0*exp(-E/R/T)*Ca#dCa/dt
    e3=Fi/A/h*(Ti-T)+J*k0*exp(-E/R/T)*Ca-Qc/p/Cp/A/h#dT/dt
    return [e1,e2,e3]
y=[]
z=[]
v=[]



def control(x,t):
    
    h=x[0]
    Ca=x[1]
    y.append(h-hs)
    v.append(t)
    Fc=F  +  Kc1*(h-hs)  +   Kc1/TTi1*trapz(y,v)
    T=x[2]
    z.append(T-Ts)
    Q=Qc  +   Kc2*(T-Ts) +   Kc2/TTi2*trapz(z,v)
    e1=(Fi-Fc)/A
    e2=Fi/A/h*(Cai-Ca)-k0*exp(-E/R/T)*Ca
    e3=Fi/A/h*(Ti-T)+J*k0*exp(-E/R/T)*Ca-Q/p/Cp/A/h
    return [e1,e2,e3]

tt=1.0
Fi=Fis
Cai=Cais
Ti=Tis
ini=fsolve(steady,[1,1,100])
[hs,Cas,Ts]=ini
figure()

while tt<10.0:
        
    F=hs/Re
    Fi=random.randint(80,120)/100.0*Fi
    Ti=random.randint(80,120)/100.0*Ti
    t=linspace(tt-1,tt,101)
    x=odeint(control,ini,t)
    subplot(221)
    plot(t,x[:,0])
    subplot(222)
    plot(t,x[:,1])
    subplot(223)
    plot(t,x[:,2])
    ini=x[-1]
    tt=tt+1

import scipy
y=scipy.array(y)
z=scipy.array(z)
err=trapz(abs(y),v)
err2=trapz(abs(z),v)
print err,err2
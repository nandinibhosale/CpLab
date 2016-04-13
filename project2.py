# -*- coding: utf-8 -*-
"""
Created on Tue Apr 05 23:08:50 2016

@author: Nandini Bhosale
"""

from scipy import linspace,exp
from scipy.optimize import fsolve
from scipy.integrate import odeint,trapz
import random
from pylab import plot,show,subplot,figure

"""PI Controller for cstr"""
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

"""Steady state calculation"""
def steady(x):
    h=x[0]
    Ca=x[1]
    F=h/Re
    T=x[2]
    e1=(Fi-F)/A
    e2=Fi/A/h*(Cai-Ca)-k0*exp(-E/R/T)*Ca
    e3=Fi/A/h*(Ti-T)+J*k0*exp(-E/R/T)*Ca-Qc/p/Cp/A/h
    return [e1,e2,e3]
    
    
y=[]
z=[]
v=[]


"""Integration using Trapz"""
def control(x,t):
    
    h=x[0]
    Ca=x[1]
    y.append(h-hs)
    v.append(t)  
    
    Fc=F+   Kc1*(h-hs)+   Kc1/TTi1*trapz(y,v)
  
    T=x[2]
    z.append(T-Ts)
    Q=Qc+    Kc2*(T-Ts)+    Kc2/TTi2*trapz(z,v)
 
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
    #Fi=random.randint(80,120)/100.0*Fi
    Ti=random.randint(80,120)/100.0*Ti
    t=linspace(tt-1,tt,11)
    x=odeint(control,ini,t)
    
    plot(t,x[:,2])
    ini=x[-1]
    tt=tt+1
show()
import scipy
y=scipy.array(y)
z=scipy.array(z)

err=trapz(abs(y),v)
err2=trapz(abs(z),v)
print err,err2

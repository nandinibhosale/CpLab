# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:44:17 2016

@author: Nandini Bhosale
"""
import scipy,scipy.optimize
from scipy.integrate import odeint
from scipy.optimize import fsolve
from scipy.optimize import fmin
from scipy import linspace,exp
from matplotlib import pyplot as plt
from numpy import array
import win32com.client
import scipy

#importing
xl = win32com.client.gencache.EnsureDispatch("Excel.Application")
wb =xl.Workbooks('ExamProblemData2.1.xlsx')
sheet=wb.Sheets('ExamProblemData')

def getdata(sheet,Range):
    data=sheet.Range(Range).Value
    data=scipy.array(data)
    data=data.reshape((1,len(data)))[0]
    return data
    
t1=getdata(sheet,"A2:A11")
t2=getdata(sheet,"D2:D11")
t3=getdata(sheet,"G2:G11")
t4=getdata(sheet,"J2:J11")
print t1

c1=getdata(sheet,"B2:B11")
c2=getdata(sheet,"E2:E11")
c3=getdata(sheet,"H2:H11")
c4=getdata(sheet,"K2:K11")

p1=getdata(sheet,"C2:C11")
p2=getdata(sheet,"F2:F11")
p3=getdata(sheet,"I2:I11")
p4=getdata(sheet,"L2:L11")



k=0.2
n=2
cao=1

def ode(c,t):
    d=-k*c**n
    return d

def solve(x):  
    x[0]=k
    x[1]=n
    t=t1
    C=odeint(ode,cao,t)
    err=scipy.array([C[0]-c1[0],C[1]-c1[1],C[2]-c1[2],C[3]-c1[3],C[4]-c1[4],C[5]-c1[5],C[6]-c1[6],C[7]-c1[7],C[8]-c1[8],C[9]-c1[9]])
    err=sum(err*err)
    return err
    
x=fmin(solve,[2,2])
x[0]=k
x[1]=n
C=odeint(ode,cao,t1)

plt.plot(t1,C)
plt.show()


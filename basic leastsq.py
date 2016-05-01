# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Nandini Bhosale\.spyder2\.temp.py
"""
import scipy,scipy.optimize,scipy.stats
import matplotlib.pyplot as plt
import numpy as np
from scipy import array
import scipy
import scipy.optimize
import scipy.stats
import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import pandas







x=scipy.array([41.5,34.5,30.57,25,22.7]) 
y=scipy.array([1.334,1.413,1.211,1.008,0.985])
yerr=scipy.array([0.0032141651,0.0046738969,0.0039605615,0.0040319298,0.0043407179])

def linear(x,p):
    [A,B]=p
    y=A*x+B
    return y
    
    
def error(p,x,y,yerr):
    err=(y-linear(x,p))/yerr
    return err
    
def r2(x,y,ycalc):
    ymean=scipy.average(y)
    dymean2=(y-ymean)**2
    dycalc2=(y-ycalc)**2
    r2=1-sum(dycalc2)/sum(dymean2)
    return r2

pguess=[2,0.1]
res=scipy.optimize.leastsq(error,pguess,args=(x,y,yerr))
print("A,B")
print res


P=res[0]
ycalc=linear(x,P)
r2=r2(x,y,ycalc)
fig=plt.figure();
ax=fig.add_subplot(111)
ax.plot(x,y,'ro');
ax.plot(x,ycalc,'b')
plt.xlabel('Height(cm)')
plt.ylabel('Resistance')
ax.title.set_text('Resistance vs height linearization'%(r2))
fig.canvas.draw()
plt.show()

M=len(y)
N=2

DFM=N-1
DFE=M-N
DFT=M-1

Y=linear(x,[0.02001567,0.558960])
Ymean=scipy.mean(y)
residuals=(Y-y)/yerr
squares=(Y-Ymean)/yerr
squaresT=(y-Ymean)/yerr

SSM=sum(squares**2)
SSE=sum(residuals**2)
SST=sum(squaresT**2)

MSM=SSM/DFM
MSE=SSE/DFE
MST=SST/DFT

R2=SSM/SST
R2_adj=1-(1-R2)*(M-1)/(M-N-1)
print R2


chisquared=sum(residuals**2)
degfreedom=M-N
chisquared_red=chisquared/degfreedom
p_chi2=1.0-scipy.stats.chi2.cdf(chisquared,degfreedom)
stderr_reg=scipy.sqrt(chisquared_red)
chisquare=(p_chi2,chisquared,chisquared_red,degfreedom,R2,R2_adj)
print chisquare








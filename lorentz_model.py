import matplotlib.pyplot as plp
import numpy as np
import math as m
import random as rr
h=0.01
czas=15
space=np.arange(0,czas,h)
leng=len(space)
x1=np.zeros(leng)
x2=np.zeros(leng)
x3=np.zeros(leng)
x1[0]=rr.random()*15
x2[0]=rr.random()*15
x3[0]=rr.random()*15


for i in range(1,leng):
    x1[i]=x1[i-1]+h*(10*(x2[i-1]-x1[i-1]))
    x2[i]=x2[i-1]+h*(28*x1[i]-x2[i-1]-(x1[i]*x3[i-1]))
    x3[i]=x3[i-1]+h*(-float(8/3)*x3[i-1]+(x1[i]*x2[i]))
plp.figure(1)
plp.plot(space,x1,'k',label='x')
plp.plot(space,x2,'b',label='y')
plp.plot(space,x3,'r',label='z')
plp.legend(loc='upper right',fontsize=14)
plp.xlabel('t-time')
plp.ylabel('state')


plp.show()
import matplotlib.pyplot as plp
import numpy as np
import math as m

h=0.001
time=55
space=np.arange(0,time,h)
leng=len(space)
x=np.zeros(leng)
y=np.zeros(leng)
a=4
x[0]=2
y[0]=2
xb=0.05
for i in range(1,leng):
    x[i]=x[i-1]+h*(pow(-x[i-1],3)+a*x[i-1]-y[i-1])
    y[i]=y[i-1]+h*(x[i]-xb)

plp.plot(space,x,'b')
plp.plot(space,y,'k')
plp.show()
import matplotlib.pyplot as plp
import numpy as np
import math as m
import scipy.optimize as opt
from openpyxl import load_workbook

##WCZYTYWANIE DANYCH Z ARKUSZA XLSX##
wb2 = load_workbook('modelowanie_systemy.xlsx', keep_vba=True)
print(wb2)
i=1
x=[]
y=[]
ktora_komurka_x='H'
ktora_komurka_y='I'
ark=wb2['Arkusz1']
while(1):
    x.append(ark[ktora_komurka_x+str(i)].value)
    y.append(ark[ktora_komurka_y+str(i)].value)
    i+=1
    if(ark['H'+str(i)].value is None):
        labelx=ark[ktora_komurka_x+str(1)].value
        labely=ark[ktora_komurka_y+str(1)].value
        print('skonczylem szukanie danych na ',i,' miejscu w arkuszu')
        break
x=np.asarray(x)
y=np.asarray(y)
##ZMIANA TYPU NA TABLICE##
#----------------------------------------------------------------------#
def model(x,a): ##WYLICZA Y z X i parametrów a
    return a.dot(x)

def wyznaczenie(x,y): # wyznaczenie parametrów a analityczną metodą najmniejszych kwadratów #
    c=x.dot(x.transpose())
    z=np.linalg.inv(c)
    return z.dot(x).dot(y.transpose())

def Q(a,xx,y): # wyznaczenie błędu średniokwadratowego #
    y_model=model(xx,a)
    Qval=np.sum(np.abs(y-y_model))
    return Qval
ilosc=len(x)
os_x=np.linspace(19.99,20.18,ilosc)
wielomian=4
Qval=[]
plp.figure(1,figsize=(10,7))
for j in range(3,wielomian):
    xwiel=np.zeros([j,len(os_x)])
    os_x_plot=np.zeros([j,len(os_x)])
    for i in range(0,j):
        xwiel[i,:]=os_x**i
        os_x_plot[i,:]=os_x**i
    a1=wyznaczenie(xwiel,y)
    os_y1=model(os_x_plot,a1)
    dict={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'a',8:'b',9:'f'}
    c="#"+str(dict[j])+"f"+str(j+7*j)+str(dict[j+1]+str(dict[j-1]))
    l='stopien wielomianu '+str(j)
    plp.plot(os_x_plot[1,:]*100,os_y1,label=l)
    plp.legend(loc='upper left')
    Qval.append(Q(a1,xwiel,y))
p = [x / 10000 for x in Qval]
print()
print("blad wynosi odpowiednio dla wielomianów od 2 do %s stopnia wielomianu"%wielomian)
print(p)
nnn=np.argmin(Qval)
print("najmniejsza wartosc bledu przy wielomianie stopnia %s"%(nnn+2))
plp.plot(os_x*100,y,color='r')
plp.xlabel('time')
plp.ylabel('millions of dolars')

plp.show()
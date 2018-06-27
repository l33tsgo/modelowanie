from openpyxl import load_workbook
wb2 = load_workbook('pomiary.xlsx', keep_vba=True)
print(wb2)
i=2 
x=[]
y=[]
xcell='D'
ycell='E'
ark=wb2['Arkusz1']
while(1):
    x.append(ark[xcell+str(i)].value)
    y.append(ark[ycell+str(i)].value)
    i+=1
    if(ark['D'+str(i)].value is None):
        labelx=ark[xcell+str(1)].value
        labely=ark[ycell+str(1)].value
        print('finished on ',i,' place')
        break

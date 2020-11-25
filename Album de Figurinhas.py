# -*- coding: cp1252 -*-
#Album de Figurinhas

N=input ('Total de figurinhas do Álbum: ')
tenho=input ('liste as figurinhas que você tem: ')
tenho=list(tenho)
total=range(1,N)
repetidas=[]
faltam=[]
I=[]
for i in tenho:
    if tenho.count(i)>=2:
        I.append(i)
        repetidas.append(i)
for I2 in set(I):
    repetidas.remove(I2)
    
for k in (set(total)-set(tenho)):
    faltam.append(k)
faltam.sort()

tenho2=[]
for t in set(tenho):
    tenho2.append(t)

print "Tenho: ", tenho2
print "Repetidas: ", repetidas
print "Faltam: ", faltam

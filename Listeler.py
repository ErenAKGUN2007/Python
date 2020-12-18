#%
#import random
from random import randint
l=[]
for _ in range(1000):
    #l.append(random.randint(50,100))
    l.append(randint(50,100))
print(l)
cift=[];tek=[]
cifto=0;teko=0
for i in l:
    if i%2==0:
        cift.append(i)
    else:
        tek.append(i)
for j in cift:
    cifto+=j
cifto/=len(cift)
for e in tek:
    teko+=e
teko/=len(tek)
print(cifto-teko)
#%
resim=[[3,7,8,7],[9,11,1,6],[14,4,2,5],[2,5]]
for b in resim:
    print(b)
for de in resim:
    for ie in de:
        print(ie)
#%
print(dir(list))
#%
ll1=[1,2]
print(ll1)
ll1.append(3)
print(ll1)
#%
ll1.clear
print(ll1)
#%
l2=[1,2,3]
print(l2)
del l2[1]
print(l2)
print(l2[1])
#% Araya sıkıştırma
l2=[1,2,3,4,5]
print(l2)
l2.insert(1,128)
print(l2)
l2.insert(-1,12)
print(l2)
#%
l2=[1,2,3,4,5]
aranan=33
if aranan in l2:
    print(l2.index(aranan))
else:
    print(f"{aranan} Listede Yok")
print(f"l2'de 42 sayından {l2.count(42)} adet var")
#%
l2=[1,2,3,4,5]
print(l2)
l2.pop()
print(l2)
def benimpop(l):
    ese=l[-1]
    del l[-1]
    return ese
#%
l2=[1,2,3,4,5]
l1=l2 #referans
l1=l2.copy() #değer
l1=l2[:] #değer
#% in-place liste içinde
l2=[5,3,2,1,4]
print(l2)
l2.reverse()
print(l2)
l2.sort()
print(l2)
l2.reverse()
print(l2)
#%silme
l2=[5,3,2,1,4]
l2s=l2.copy()
del l2
print(l2s)
l2s.reverse()
print(l2s)
l2s.sort()
print(l2s)
l2s.reverse()
print(l2s)
#% list compraesionsfdgdgfd
sifirlar=[i for i in range(8)]
print(sifirlar)
sifirlar=[i*0 for i in range(8)]
print(sifirlar)

kareler=[i*i for i in range(1,99)]
print(kareler)
#%
#ikib=[[i*j for j in range(1,5)] for i in range(1,31)]
ikib=[[3*i+1+j for j in range(0,3)] for i in range(0,3)]
print(ikib)

sayilar=[]

#%
listem=[randint(1,1000) for _ in range(100)]
ciftler=[i for i in listem if i%2==0]
tekler=[i for i in listem if i%2==0]
k500=[i for i in listem if i<=500]
b500=[i for i in listem if i>500]
print(f"Sayılar: {listem}")
print(f"Tek Sayılar: {tekler}")
print(f"Çift Sayılar: {ciftler}")
print(f"500'e Eşit Veya Küçük Sayılar: {k500}")
print(f"500'den Büyük Sayılar: {b500}")

#%numpy/pandas
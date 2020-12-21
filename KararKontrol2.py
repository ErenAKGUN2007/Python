#% 24 ekim
r1=range(1,30,2)
print(r1[2])
for sayi in r1:
    print(sayi)
#%
demet1=range(1,30,1),range(30,20,-1)
for a in demet1:
    for b in a:
        print(b)
#%
i=0
while i<10:
    print(i)
#%
r=range(1,10,1)
i=0
while i<len(r):
    print(r[i])
    i+=1
#%
bolunen=47
bolen=3
kalan=0
bolum=0
while bolunen>bolen:
    bolunen-=bolen
    bolum+=bolen
kalan=bolunen
print(f"Bolum: {bolum} Kalan: {kalan}")
# % iç içe while

i=1;j=1

while i<=3:
    j=i
    while j<=3:
        print("i*j=",i*j)
        j+=1
    # j=1
    i+=1
 

# % en büyükn alt dizi
dizi=[13, -3, -25,20, -50, -3, -3, 23, 50, 20, -50, -12, -5, -22, -15, -4, -7]
#en önemli örnek
i=0
j=0
enKarli=-1000000000# eksi sonsuz
suanki=0
bas=0
bit=0

while i<len(dizi):
    j=i
    while j<len(dizi):
        # print(dizi[i],dizi[j],sep="#")
        suanki+=dizi[j]
        if suanki>enKarli:
            enKarli=suanki
            bas=i
            bit=j
        j+=1
    suanki=0
    i+=1
print(enKarli,bas,bit)
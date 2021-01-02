#%
#sayi=float(input("Sayi Gir: "))
#if sayi>0:
#    print("Sayi Pozitif")
#elif sayi<0:
#    print("Sayi Negatif")
#else:
#    print("Sayi Pozitif Ya Da Negatif Değil")
# %
#dz=21.0
#ort=79
#zayif=1
#if dz<=20.0 and (ort>75.0 or zayif<=3):
#    print("Geçti")
#else:
#    print("Kaldı")
# %
#% if-elif-else

sayi=float(input("sayı gir:"))

# if sayi>0:
#     print("pozitif")
# if sayi==0:
#     print("sayı sıfır")
# if sayi<=0:
#     print("sayı negatif")


if sayi>0:
    print("pozitif")
elif sayi==0:
    print("sayı sıfır")
elif sayi==-2:
    print("sayı -2")
elif sayi==-2:
    print("sayı -3")
else:
    print("sayı negatif")



# % and or not şart birleştirme

dz=21.0
notort=79.0
zayifSayisi=1

#devamsızlık 20 günden fazla ise kesin kalır
#3ten fazla zayıfı var ama not ort 75ten büyükse kalır
#diğer her durumda geçer

if dz<=20.0 and (notort>75.0 or zayifSayisi<=3):
    print("geçer")
else:
    print("kalır")



# %
a=2;d=3;e=8
print(a,d,e)
# % döngü for döngüsü

l=[[10,20],20,[3,50,8],(1,2,3)]

for i in l:
    if isinstance(i,list):
        for t in i:
            print(t)
    else:
        print(i)


ad="hasan"
for harf in ad:
    print(harf)

# %  for liste

l3=[1,2,3]
for e in l3:
    e=5
print(l3)


# % range komutu

#range(sayi)
print(range(5))

aralik=range(10)

for i in aralik:
    print(i)

#range(s1,s2)

print(range(12,55))
for i in range(12,20):
    print(i)

#range(s1,s2,s3)

print(range(20,30,2))

for i in range(30,22,-1):
    print(i)

# for i,j in range(1,10),range(1,10):
#     print(i,j)

# for i in range(10.0,20.0,0.5):
#     pass
# %

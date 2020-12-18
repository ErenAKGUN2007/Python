#l=[i for i in range(1,21)]
#print(l)

#% %
#import random
#import matplotlib.pyplot as plt
#isim=["A","B","C","D","E"]
#s=[]
#for _ in range(len(isim)):
#    s.append(random.randint(0,100))
#plt.bar(isim,s)
#plt.show()

# %% listeler
l1=[]  # boş liste **
l2=list()  # boş liste

ogler=["ahmet efe", "zeynep", "reyyan", "yusuf", "mert",
         "kerem", "tarık"]
mix=[1, 2, 32.0, "hasan", True, True, False]

print(ogler)
print(mix)
print(ogler[1])
ogler[3]="yusuf aras"
print(ogler)

for isim in ogler:
    print(isim)


# %%
#karakter dizisi koleksiyon
#mutable--değişebilir immutable değişemez

isim="reyyan/tarık"

for harf in isim:
    print(harf)

print("3. eleman",isim[3])

#isim[3]="h" #immutable HATA

isim="fatih"


# %% in komutu

kelime="merhaba"

sonuc="er" in kelime
print(sonuc)

# %%

print(kelime)
print(kelime[0:2])#ilk iki
print(kelime[0:4])
print(kelime[-1])# son eleman
print(kelime[3:])#3. elemandan sona kadar
print(kelime[:3])#baştan 3 karakter
print(kelime[3:len(kelime)])
print(kelime[-3:-1])
print(kelime[::2])#baştan iki atlayarak
print(kelime[::-1])#tesrten birer birer

# %%  ilkel tip (primitive)
#ilkel tipler değer tutar ve değer aktarır

sayi1=30
sayi2=sayi1

print("sayi1=",sayi1,"sayi2=",sayi2)
sayi1=25
print("sayi1=",sayi1,"sayi2=",sayi2)
# %% referans tipler
#referans tipler adres  aktarır.

nums=[1,2,3,4]
sayilar=nums#nums[:] bu kullanım sadece değerleri aktarır
print("nums=",nums,"sayilar=",sayilar,sep="\n")

nums[3]=18
print("nums=",nums,"sayilar=",sayilar,sep="\n")
# %% liste fonskiyonları

import random

notlar=[]

for _ in range(5):
    notlar.append(random.randint(50,100))

print(notlar)
isimler=["arda","ahmet","zeynep","reyyan","mert","serkan"]
print(isimler)
print(isimler.count("arda"))
isimler.remove("serkan")
print(isimler)


# %%
import random
import matplotlib.pyplot as plt
notlar=[]

for _ in range(5):
    notlar.append(random.randint(50,100))
isimler=["arda","ahmet","zeynep","reyyan","mert"]

plt.xlabel("isimler")
plt.bar(isimler,notlar)
plt.show()

# %% 
l1=[1,2]
t1=(1,2)
s1={1,1,1,2,6,892,29,98,498,48718,98,7,8,6,2,65,4,2,6,5,2}



#%%
d1={1:"isim1","2":"ffxg",100.2:"3"}
print(d1)
print(d1[1])
print(d1["2"])
# %% Dictionary (key, value)

l1=[1,2]
t1=(1,2)
s1={1,2,3,3,3,3,2,5,6,7,7,6,1}
print(type(s1))
print(s1)
# %% Sözlük tanımlama
d1={100:"serkan",2:"eren",3:"kayra",4:"levent","5":"arda",
6.0:"olcay",7:"atahan",8:"yaman"}

print(d1)
print(d1[100])
print(d1["5"])
# %%  sınıf bilişim notları tutalım

notlar={"hasan":[95,98,100],"yaman":[100,100,[1001,98]]}

print(notlar["hasan"])
print(notlar["hasan"][1])
print(notlar["yaman"][2][0])
print(notlar["yaman"][1:])
# %% sözlükteki anahtarları 
print(notlar.keys())

for k in notlar.keys():
    print(k)
print("hasan" in notlar)
for k in notlar:
    print(k)

print(notlar.values())

# %% ekleme silme

d3={1:10,2:20,30:25,20:12}
d3[38]=42
print(d3)

del d3[30]
print(d3)

# a=5
# print(a)
# del a
# print(a)

d3.clear()
print(d3)
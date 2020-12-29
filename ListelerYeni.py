####listeler ayrıntılı######

# % diziler neden lazım(liste)
import random
d1=random.randint(0,1000)
d2=random.randint(0,1000)
#98 satır daha

rastgeleSayilar=[] #list() boş liste
for i in range(100):
    tutulan=random.randint(0,1000)
    rastgeleSayilar.append(tutulan)

print(rastgeleSayilar)
# % 
sayilar=[1,2,51,36,25,23]
print(sayilar[0]+sayilar[1]+sayilar[2])

print("sayilar listesinde ",len(sayilar)," eleman vardır")

print(sayilar)
del sayilar[3]
print(sayilar,"\neleman sayısı=",len(sayilar))
# % çok boyutlu diziler
resim=[[200,202,38,42],[30,25,40,187],[30,22],[2,78,85,155]]
print(resim[0])
print(resim[0][1])
print(resim[2][1])
# % liste boyutları
l1=[1,2,3]
l2=[[1],[2],[3]]
print(l1[1]+1)
print(l2[1]+1) # bu satır hata verir int ile list toplanamaz
print(l2[1][0]+1)

# %

l2=[2,3,68,3]

for e in l2:
    print(e)

# % çok noyutlu dizilerde dolaşma
reyon=[[200,202,38,42],[30,25,40,187],[30,22],[2,78,85,155]]
for e in reyon:
    print(e,end="-->")
    print(type(e))


# %
reyon=[[200,202,38,42],[30,25,40,187],
[30,22],[2,78,85,155]]
for e in reyon:
    for t in e:
        print(t,end=" ")
    print()

# %
reyon=[[200,202,38,42],[30,25,40,187],
[30,22],[2,78,85,155]]

#acaba hangi reyondaki ününlerin fiyat toplamı daha büyük

r0=0
for fiyat in reyon[0]:
    r0+=fiyat
print(r0)
r1=0
for fiyat in reyon[1]:
    r1+=fiyat
print(r1)
r2=0
for fiyat in reyon[2]:
    r2+=fiyat
print(r2)
r3=0
for fiyat in reyon[3]:
    r3+=fiyat
print(r3)


# % dir komutu
# bir tip/tür yapısında bulunan fonksiyonları gösterir

print(dir(list))
print(10*"-")
print(dir(int))

# % 

print(dir(list))
# % append listenin en sonuna eleman ekler
l=[1,2,3]

l.append("serkan")
l.append(38.5)
print(l)
#clear komutu listeyi temizler elemanlarını siler
#l.clear()
print(l)

# % count aranılamn elemandan kaç tane var 
# o değeri cevap olrak döndürür

l=[1,21,3,33,14,12,33,[33,33,33]] 
print(l.count(33))
print(l.count([33,33,33]))
print(l[7].count(33))

# % index aranılan elamnın indis numrasını verir
# aranan eleman yoksa hata verir.
print(l.index(33))
# print(l.index(333)) hata verir
aranan=333

if aranan in l:
    print(l.index(aranan))
else:
    print("aranan",aranan,"değeri, listede yok")


# % insert belirtilen index numrasına eleman ekler
l= [1,2,3]
l.append(4)
print(l)
l.insert(1,70)
print(l)
for _ in range(3):
    a=int(input("değer gir"))
    l.insert(0,a)
    print(l)

# % pop komutu en son elemanın değerini gönderir
# ve en son elemanı siler

# yığın(stack)
arabalar=[]
arabalar.append("hyundai i20")
print(arabalar)
arabalar.append("honda civic")
print(arabalar)
arabalar.append("vw golf")
print(arabalar)

print(arabalar.pop())
print(arabalar.pop())
print(arabalar.pop())
print(arabalar)

# %
# kuyruk(queue)
arabalar=[]
arabalar.insert(0,"hyundai i20")
print(arabalar)
arabalar.insert(0,"honda civic")
print(arabalar)
arabalar.insert(0,"vw golf")
print(arabalar)

print(arabalar.pop())
print(arabalar.pop())
print(arabalar.pop())
print(arabalar)
# %
dir(list)

# % benim pop fonksiyonun

l1=[1,2,3,4]
l2=[1,2,3,4,5]
l3=[1,2,3,4,5,6]
# print(l1[-1])
# print(l2[-1])
# print(l3[-1])
def benimpop(liste):
    lse=liste[-1]
    del liste[-1]
    return lse
print(l3)
print(benimpop(l3))   
print(l3)
print(benimpop(l3))   
print(l3)
print(benimpop(l3))   
print(l3)
# % ilkel değerler fonksiondan etkilenmez

a= 10

def ikikatı(s):
    s=s*2
    print(s)

print(a)
ikikatı(a)
print(a)
# % sıralama(sorting) ve ters çevir(reversing)
#in-place demek verilen liste üzerinde
# değişiklik yaplılır
l=[3,5,78,1,199,54,0,4]
print(l)
l.sort()
print(l)
l.reverse()
# küçükten büyüğe ascending
# büyükten küçüğe descending

# % sıralam
l_d=["3","5","78","1","199","54","0","4","9"]
l_d.sort()
print(l_d)

# % in-place örneği

def ip_2kat(lst):
    i=0
    while i<len(lst):
        lst[i]=lst[i]*2
        i+=1

l=[3,5,78,1,199,54,0,4]
print(l)
ip_2kat(l)
print(l)

# % out-place
def op_2kat(lst):
    i=0
    yl=[]
    while i<len(lst):
        yl.append(lst[i]*2)
        i+=1
    return yl

l=[3,5,78,1,199,54,0,4]
print(l)
dl=op_2kat(l)
print(l)
print(dl)
# % list comprhesion
l_z=[i for i in range(1,10)]
print(l_z)

l_z1=[0 for i in range(10)]
print(l_z1)

l_z2=[i*i for i in range(1,10)]
print(l_z2)

# % içi -1 lerle dolu 5*5 lik bir liste
skl=[]

skl=[[-1 for t in range(5)] for i in range(5)]
print(skl)
print(10*"*")
listem=[]
e=[]
for i in range(5):
    for t in range(5):
        e.append(-1)
    listem.append(e.copy())
    e.clear()
print(listem)

# % 1-9 arasında sayılardan oluşan 3*3 lük dliste
listem=[[ 3*i+1+j for j in range(0,3)]for i in range(0,3)]
print(listem)
# % 100 elemanlı 
# 1-1000 arası rastgele sayılardan  oluşan liste
import random
l2=[random.randint(1,1000) for _ in range(100)]
print(l2)

# % l2 listesindeki çift ve tek sayıları ayrı birer
# listeye aktarcam
print("l2:\n",l2)

ciftler=[sayi for sayi in l2 if sayi%2==0]
print("çiftler:\n",ciftler)
tekler=[sayi for sayi in l2 if sayi%2==1]
print("tekler:\n",tekler)
#%
# l2 deki 500den küçük ve 500 e eşit olan sayıları bir gruba
# 500 den büyük olanları bir listeye

kucuk500=[sayi for sayi in l2 if sayi<=500]
print("500'den küçük",kucuk500)
buyuk500=[sayi for sayi in l2 if sayi>500]
print("500'den büyük",buyuk500)
#% liste toplama
a=[1,2,3]
b=[4,5,6]
c=a+b #1,2,3,4,5,6
#c=a+33+b hate
c=a+[33]+b #1,2,3,33,4,5,6

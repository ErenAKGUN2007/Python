#%
# Miras Alınmayacaksa "class IlkSinif:" da olabilir
class IlkSinif():
    a=5
o1=IlkSinif()
print(o1.a)

#%
class Insan():
    def __init__(self,k,b,sr): #Self yerine herhangi Birşey gelebilir.
        self.kilo=k
        self.boy=b
        self.sacRengi=sr
    def yemek_ye(self,miktar):
        self.kilo+=miktar
    def spor_yap(self,sporun_verdirdigi_kilo):
        self.kilo-=sporun_verdirdigi_kilo
    def bki(self):
        #self.bki=self.kilo/self.boy**2
        return self.kilo/self.boy**2
i1=Insan(75,1.74,"Kahverengi")
i1=Insan(35,1.65,"Siyah")
print(i1.boy)
print(i1.kilo)
print(i1.sacRengi)
i1.yemek_ye(2)#kiloluk yemek
print(i1.kilo)
i1.spor_yap(12)#kiloluk spor
print(i1.kilo)
print(i1.bki)

a=5
print(id(a)) #ram adresi
a=5.0
print(id(a)) 
a="5.0"
print(id(a))
#% oopde sahip olma drumuna göre değişkenler
#   1 nesnelere ait değişkener:
class kedi:
    def __init__(self,ad="<yok>",renk="sayı",kilo=5):
        self.isim=ad
        self.renk=renk
        self.__kilo=kilo # iki alt çizgi değeri korur/gizler(kapsülleme)
        print(f"{self.isim} adında, {self.renk} renkli, {self.__kilo} ağırlığında bir kedi oluştu.")
        #nesne değişkenleri
    def __del__(self):
        print(f"{self.isim} kedisi silindi.")
    def ses(self):
        print(f"{self.isim}: Miyav!")
    def setkilo(self,kilo):
        if kilo>0:
            self.__kilo=kilo
            print("Kilo Ayarlandı.")
        else:
            #print("Kilo Çok Düşük.")
            self.__kilo=-kilo
            print("Kilo Ayarlandı.")
    def getkilo(self):
        return self.__kilo
k1=kedi("Tekir","siyah",-5)
k2=kedi(renk="Bayaz")
k3=kedi("karagöz")
print(k1.isim)
print(k1.renk)
#print(k1.__kilo)
print(k1.getkilo())
k1.setkilo(12)
print(k1.getkilo())
k1.setkilo(-3)
k1.ses()
print(k1.getkilo())
#%yığın(stack)
class Yigin:
    def __init__(self):
        self.__liste=[]
    def push(self,deger):
        self.__liste.append(deger)
    def pop(self):
        s=self.__liste.pop()
        return s
    def dondur(self):
        for i in self.__liste:
            print(i)
y1=Yigin()
y1.push(10)
y1.push(20)
y1.push(30)
y1.push(40)
y1.push(50)
y1.push(60)
y1.dondur()
print(y1.pop())
print(10*"-")
y1.dondur()

#%kuyruk
class Kuyruk:
    def __init__(self,*degerler):
        self.__liste=[]
        for i in degerler:
            self.__liste.append(i)
    def push(self,deger):
        self.__liste.append(deger)
    def pop0(self):
        s=self.__liste.pop(0)
        return s
    def dondur(self):
        for i in self.__liste:
            print(i)
print(50*"-")
k1=Kuyruk()
k1.push(10)
k1.push(20)
k1.push(30)
k1.push(40)
k1.push(50)
k1.push(60)
k1.dondur()
print(k1.pop0())
print(10*"-")
k1.dondur()
#%
def notHesapla(adi:str,soyadi:str,*notlar):#notlar:tuple
    ort=0
    for nt in notlar:
        ort+=nt
    return ort/len(notlar)
    print(ort/len(notlar))
notHesapla("Ad","Soyad",100)
notHesapla("Ahmet","Bilmemkim",100,80,90,77,66,35)
#%
def f1(a,b,*c,**d):
    print(f"c:{type(c)} deger:{c}")
    print(f"d:{type(d)} deger:{d}")
f1(1,3656,49,449,95,6,6,1,23,1,21,54)
#%
a={1:"8",2:"10"}
print(list(a.keys()))
print(list(a))
print(list(a.values()))
ll=[0,1]
""" #devamı yok """

#% snıfa ait özellik ve davranışlar
class hayvan:
    adet=0
    ayaksayisi=4
    def __init__(self,ad="<yok>",renk="sayı",kilo=5):
        self.isim=ad
        self.renk=renk
        self.__kilo=kilo # iki alt çizgi değeri korur/gizler(kapsülleme)
        print(f"{self.isim} adında, {self.renk} renkli, {self.__kilo} ağırlığında bir kedi oluştu.")
        #nesne değişkenleri
    @classmethod
    def arttir(cls):
        cls.adet+=1
    def __del__(self):
        print(f"{self.isim} kedisi silindi.")
    def ses(self):
        print(f"{self.isim}: Miyav!")
    def setkilo(self,kilo):
        if kilo>0:
            self.__kilo=kilo
            print("Kilo Ayarlandı.")
        else:
            #print("Kilo Çok Düşük.")
            self.__kilo=-kilo
            print("Kilo Ayarlandı.")
    def getkilo(self):
        return self.__kilo
print(dir(hayvan))

class hesap:
    degerler=[0]
    @classmethod#sınıfa ait özellik
    def topla(cls):
        toplam=0
        for a in cls.degerler:
            toplam+=a
        return toplam

hesap.degerler.append(3)
hesap.degerler.append(3)
hesap.degerler.append(3)
hesap.topla()
#%
class Araba:
    adet=0
    def __init__(self,renk="<Boyasız>",marka="<Markasız>",model="<Modelsiz>"):
        self.boyarengi=renk
        self.marka=marka
        self.model=model
        self.adetarttir()
    def renkDegistir(self,yenirenk:str):
        self.boyarengi=yenirenk
    @classmethod
    def adetarttir(cls):
        cls.adet+=1
    def __del__(self):
        print("Bir Araba Silindi.")
        self.adet-=1
arabalar=[]
for _ in range(30):
    araba=Araba()
    arabalar.append(araba)
#% sınıfa ait methodalr @classmethod la tanımlanır
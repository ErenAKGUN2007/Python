print("Merhaba Dünya")
def ikinci():
    print("Merhaba")
ikinci()
def selam(isim):
    print(f"Merhaba {isim}!")
selam("Eren")
def dortgenAlani(k,u):
    print(k*u)
dortgenAlani(25,65)
def merhaba(ad,soyad):
    print(f"Merhaba {ad} {soyad}")
merhaba("Eren","AKGÜN")
merhaba(soyad="AKGÜN",ad="Eren")
def hesapla(a,b,c,d):
    sonuc=a+b*c/d
    print(sonuc)
hesapla(1,2,10,2)
hesapla(a=1,d=8,b=4,c=10)
hesapla(a=1,c=10,d=8,b=4)
hesapla(1,2,d=5,c=8)
#hesapla(1,2,d=5,b=8) Hata

# Değer Döndürme
def daireAlan(yaricap):
    return 3*yaricap*yaricap
alan=daireAlan(3.0)
print(f"Daire Alanı: {alan}")
l={1,2,3,9,78,59,12}
def listeToplam(liste):
    t=0
    for i in liste:
        t+=i
    print(t)
    return t
listeToplam(l)
def artikYilmi(yil):
    if yil%100==0:
        if yil%400==0:
            return True
        else:
            return False
    elif yil%4==0:
        return True
    else:
        return False
print(artikYilmi(2020))

def asalmi(sayi:int):
    tf=True
    for i in range(2,sayi//2+1):
        if sayi%i==0:
            tf=False
            break
    return tf
print(asalmi(35))

def hacim(a,b=2,c=8):
    return a*b*c
print(hacim(1,5,3))
print(hacim(1))
print(hacim(1,5))
#geçerlik alanı
def dsff():
    x=10
    print(x)
dsff()
#print(x)
y=10
def dddd():
    print(y)
dddd()
def kkkk():
    global xyz
    xyz=10
    print(xyz)
kkkk()
print(xyz)
#ucgen alani hesaplama (Heron)
def ucgenMi(x,y,z):
    return x+y>z and x+z>y and y+z>x
def ualan(a,b,c):
    if ucgenMi(a,b,c):
        s=(a+b+c)/2
        ua=(s*(s-a)*(s-b)*(s-c))**0.5
        return ua
    else:
        return False
print(ualan(3,4,5))
print(f"Ucgen:    {ualan(5,6,7)}")
#faktöriyel
def faktoriyel(s):
    if s>0 and s==int(s):
        f=1
        for i in range(1,s+1):
            f=f*i
        return f
print(f"faktoriyel5={faktoriyel(5)}")
#metin arama
def metinara(metin,aranan):
    if aranan in metin:
        return True
    return False
print(metinara("Bu Bir Test Yazısıdır.","zısı"))
#metin uzunluğu2
def mvarmi(met,aran):
    mu=len(met)
    au=len(aran)
    i=0
    while i<=mu-au:
        j=0
        while j<au:
            if met[i+j]==aran[j]:
                j=j+1
                continue
            else:
                break
            j=j+1
        if j==au:
            return True
        i=i+1
print(mvarmi("test yazısı","zıs"))

def metin_varMi(metin,aranan):
    mu=len(metin)
    au=len(aranan)
    i=0
    j=0
    while i<=mu-au:
        j=0
        while j<au:
            if metin[i+j]==aranan[j]:
                j+=1
                continue
            break
        if j==len(aranan):
            return True
        i+=1
    return False

m="abracadabra"
a="ca"
print(metin_varMi(m,a))
#fibonacci
def fib(adim:int):
    if adim==1:
        return 1
    elif adim<1:
        return 0
    else:
        return fib(adim-1)+fib(adim-2)
print(fib(10))


def fibur(adim:int):
    if adim==0:
        return None
    elif adim<3:
        return 1
    else:
        f1=f2=1
        for _ in range(3,adim+1):
            f1,f2=f2,f1+f2
        return f2 
print(fibur(1000))
print(fibur(1000)/fibur(999))
fib=[]
for i in range(0,1000):
    fib.append(fibur(i))
print(fib)
#%%
t=0
while True:
    sayi=input("Sayı Gir: ")
    if sayi=="q":
        print(f"Toplam: {t}")
        break
    t=t+int(sayi)
#%%
t=0
while True:
    sayi=input("Sayi Gir: ")
    if sayi=="q":
        print(f"Toplam: {t}")
        break
    try:
        t=t+int(sayi)
    except:
        print("Hata")
#%%
unlu="eaiıuüoö"
metin="Bu Bir Test Yazısıdır."
t=0
for harf in metin:
    if harf in unlu:
        t+=1
    else:
        continue
print(t)
#%%
t=0.0
l=[1,2,3,4,5,6]
for i in l:
    if i!=3:
        t+=1/(3-i)
#for i in l:
#    if i==3:
#        continue
#    else:
#        t+=1/(3-i)
print(t)
#%%
t=0.0
i=0
l=[1,2,3,4,5,6]
while i<len(l):
    t+=1/(3-l[i])
    i+=1
print(t)
#%%
c0=int(input("Sayi Gir: "))
a=0
while c0!=1:
    a+=1
    if c0%2==0:
        c0=c0/2
    else:
        c0=3*c0+1
print(a)
# %%
i=1
while i<10:
    print(i)
    i+=1
else:
    print(i)
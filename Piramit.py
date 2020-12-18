sayi=int(input("Blok Sayısı: "))
i=1
while True:
    sayi=sayi-i
    if sayi==0:
        break
    if sayi<0:
        i-=1
        break
    i+=1
print(f"Piramit Yüksekliği: {i}")
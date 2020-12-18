dizi=[43,4,17,42,2,36,20,30,22,50,60]
for i in range(len(dizi)):
    b=dizi[i]
    for a in range(len(dizi)):
        c=dizi[a]
        if b%c==0:
            if b!=c:
                print(b,"-",c)
for i in dizi:
    for a in dizi:
        if i%a==0 and i!=a:
                print(f"{i} - {a}")
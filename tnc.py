#Türkçe Karakter Yok
#Sözlüğü kısaltmayı denedim ama olmadı belki bir yolu vardır. "A","B","C","a","b","c":2 gibi
#harfler={"A":2,"B":2,"C":2,"D":3,"E":3,"F":3,"G":4,"H":4,"I":4,"J":5,"K":5,"L":5,"M":6,"N":6,"O":6,"P":7,"Q":7,"R":7,"S":7,"T":8,"U":8,"V":8,"W":9,"X":9,"Y":9,"Z":9,"a":2,"b":2,"c":2,"d":3,"e":3,"f":3,"g":4,"h":4,"ı":4,"j":5,"k":5,"l":5,"m":6,"n":6,"o":6,"p":7,"q":7,"r":7,"s":7,"t":8,"u":8,"v":8,"w":9,"x":9,"y":9,"z":9}
harfler={"A" or "B" or "C":2,"D" or "E" or "F":3,"G":4,"H":4,"I":4,"J":5,"K":5,"L":5,"M":6,"N":6,"O":6,"P":7,"Q":7,"R":7,"S":7,"T":8,"U":8,"V":8,"W":9,"X":9,"Y":9,"Z":9,"a":2,"b":2,"c":2,"d":3,"e":3,"f":3,"g":4,"h":4,"ı":4,"j":5,"k":5,"l":5,"m":6,"n":6,"o":6,"p":7,"q":7,"r":7,"s":7,"t":8,"u":8,"v":8,"w":9,"x":9,"y":9,"z":9}
sayilar=["0","1","2","3","4","5","6","7","8","9","-"]#Alt Çizgi İle Tekrar Uğraşmamak İçin
####def phone_converter(phone_alpha):
    j=0
    yeni=""
    for i in phone_alpha:
        j+=1
        if ((j==4 or j==8) and i!='-') or ((not (j==4 or j==8)) and i=='-') or len(phone_alpha)!=12 or ((not i in sayilar) and (not i in harfler)):
            return -2
        elif i in sayilar:
            yeni+=i
        elif i in harfler:
            yeni+=str(harfler[i])
    if phone_alpha==yeni:
        return -1
    return yeni
print(phone_converter("555-GET-FOOD"))#Değişmiş
print(phone_converter("310-EAT-MeaT"))
print(phone_converter("EAT-123-MEAT"))
print(phone_converter("010-123-9876"))#-1
print(phone_converter("310-EAT-CHICKEN"))#-2
print(phone_converter("310-EATMEAT"))
print(phone_converter("310-123456"))
print(phone_converter("310-123-456"))
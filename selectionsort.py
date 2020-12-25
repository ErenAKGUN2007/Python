from random import randint as random
def enkucugubul(dizi):
    enkucuk=dizi[0]
    enkucukyer=0
    for i in range(1,len(dizi)):
        if dizi[i]<enkucuk:
            enkucuk=dizi[i]
            enkucukyer=i
    return enkucukyer
def selectionSort(dizi):
    sirali=[]
    for _ in range(len(dizi)):
        eky=enkucugubul(dizi)
        sirali.append(dizi.pop(eky))
    return sirali
if __name__=="__main__":
    sirasizd=[random(1,1000) for i in range(20)]
    print(sirasizd)
    print(10*"-")
    print(selectionSort(sirasizd))
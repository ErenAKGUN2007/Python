from random import randint as random
def quickSort(dizi):
    if len(dizi)<2:
        return dizi
    else:
        pivot=dizi[0]
        sol=[i for i in dizi[1:] if i<=pivot]
        sag=[i for i in dizi[1:] if i>pivot]
        return quickSort(sol)+[pivot]+quickSort(sag)
if __name__=="__main__":
    sirasizd=[random(1,1000) for i in range(20)]
    print(sirasizd)
    print(10*"-")
    print(quickSort(sirasizd))
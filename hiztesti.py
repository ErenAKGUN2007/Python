from quicksort import quickSort
from selectionsort import selectionSort
from datetime import datetime as saat
from random import randint as random
#print(saat.now())
liste=[random(1,1_000_000_000) for _ in range(20_000)]
selection=liste.copy()
quick=liste.copy()
python=liste.copy()
_1=saat.now()
quickSort(quick)
_2=saat.now()
selectionSort(selection)
_3=saat.now()
python.sort()
_4=saat.now()
print(f"Quick    : {_2-_1}\nSelection: {_3-_2}\nPython   : {_4-_3}")
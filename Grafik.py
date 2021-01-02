import matplotlib.pyplot as plt
#import numpy as np
x=[]
y=[]
for i in range(-100,101,1):
    x.append(i)
for t in x:
    islem=((t**2)*2)-(t*3)-5
    y.append(islem)
plt.plot(x,y)
#plt.savefig("Eren_AKGÜN2.png")
plt.show()
#2x^2 - 3x - 5
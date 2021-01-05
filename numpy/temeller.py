import numpy as np
l1=np.zeros(100_000_000)
print(l1.size)
print(l1.shape)
print(l1.dtype)
print(l1.ndim)
del l1


#Şekil düzgün olmalı
liste=[1,2,3]
nd1=np.array(liste,dtype=np.byte)
print(nd1.size)
print(nd1.shape)
print(nd1.dtype)
print(nd1.ndim)
print(type(nd1))

print(nd1[2])
#%boyutlar
#0D
nd2=np.array(38)
print(nd2.size)
print(nd2.shape)
print(nd2.dtype)
#1D
nd3=np.array([1,2,3])
print(nd3.size)
print(nd3.shape)
print(nd3.dtype)
#2D
nd4=np.array([[1,2,3]],dtype=np.uint8)
print(nd4.size)
print(nd4.shape)
print(nd4.dtype)
#3D
nd5=np.array([[[1,2,3],[1,2,3]]])
print(nd5.size)
print(nd5.shape)
print(nd5.dtype)
#slice
nd6=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(nd6.size)
print(nd6.shape)
print(nd6.dtype)
print(nd6[0,])
print(nd6[1,])
print(nd6[:,3])
print(nd6[:,2])
print(nd6[2:,1:3])
print(nd6[0:2,2:])
#kırpma
import cv2,os
cd =  os.getcwd()
resim_yolu = os.path.join(cd,"numpy","test.png")
image = cv2.imread(resim_yolu)
image_cut = image[0:250,600:800,:]
cv2.imshow("resim",image_cut)
cv2.waitKey(0)
#arange,randint,linspace,zeros,ones,full


pass

#Elemalara Ulaşma


pass


#arange=range
ndt1=np.arange(12)
print(ndt1)
ndt1[3]=333
print(ndt1)

#0lardan 3,3,3 dizi
ndz0=np.zeros((3,3,3),dtype=np.float32)
print(ndz0)
ndz0[0,1,1]=33
print(ndz0)
#1lerdan 3,3,3 dizi
ndo0=np.ones((3,3,3),dtype=np.float32)
print(ndo0)
ndo0[0,1,1]=33
print(ndo0)
#full
ndf0=np.full((3,3,3),123)
print(ndf0)
#randint=random.randint
ndr0=np.random.randint(0,255,(4,4),dtype=np.uint8)
print(ndr0)
print(10*"*")
ndr0[1]=255
print(ndr0)
#slice
ndr1=np.arange(12)
print(ndr1.shape)
ndr1.shape=(3,4)
print(ndr1.shape)
print(ndr1)
print(f"\n{ndr1[0,:]}")#1D
print(f"\n{ndr1[0:1,:]}")#2D

# % slice biçme iişlemleri
ndr1 = np.arange(12)
print(ndr1.shape)
ndr1.shape=(3,4)# bu komut dizi şeklkini değiştirdi
print(ndr1.shape)
print(ndr1)
print("\n",ndr1[0,:])#0. satırı verir
print("\n",ndr1[0:1,:])#0. satırı 2 boyutlu olarak verir
print("\n",ndr1[0:2,:])#0. satırı 2 boyutlu olarak verir
print("\n",ndr1[2,2:])#2. satırdaki 2.sütun sonrası
print("\n",ndr1[1:,1:3])


# %
# % kopya ve görüntü (copy and view)
# Bir dizinin kopyası ile görünümü arasındaki temel fark, kopyanın yeni bir dizi olması ve görünümün yalnızca orijinal dizinin bir görünümü olmasıdır.

# Kopya(copy) verinin sahibidir ve kopyada yapılan herhangi bir değişiklik orijinal diziyi etkilemeyecektir ve orijinal dizide yapılan herhangi bir değişiklik kopyayı etkilemeyecektir.

import numpy as np
n15 = np.array([1, 2, 3, 4, 5])
x = n15.copy()# hiçbirşeyden etkilenmemek için
y = n15.view()# ana kopyadaki değişiklik diğerlerine de etki etsin istenirse view
n15[0] = 42

print(n15)
print(x, "--", x.base)
print(y, "--", y.base)

x[4] = 55
y[3] = 44
print(20*"-")
print("n15:", n15)
print("x:", x, "--", x.base)
print("y:", y, "--", y.base)

# % skalare işlemler
import numpy as np

a = np.array([[1, 2],[3, 4]])
b = np.array([[40, 30],[20, 10]])

print("skaler işlemler:")
print("a+1:",a+1,end="\n\n")
print("a*2:",a*2,end="\n\n")
print("b/3:",b/3,end="\n\n")
print("b-2:",b-2,end="\n\n")
print("np.sgrt(a):",np.sqrt(a),end="\n\n")
print("a*a:",a*a,end="\n\n")
print("a+b:",a+b,end="\n\n")# ayı şekle sahip olanlar da 4 işlem yapılabilir.
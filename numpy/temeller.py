import numpy as np
liste=[1,2,3]
nd1=np.array(liste,dtype=np.byte)
print(nd1.size)
print(nd1.shape)
print(nd1.dtype)

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
nd4=np.array([[1,2,3]])
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
#rastgele resim
import cv2
import numpy as np
image=np.random.randint(0,255,size=(600,600,3),dtype=np.uint8)#tek renk için size son değeri 1 olmalı
cv2.imshow("Rastgele",image)
cv2.waitKey(0)
#kırpma
import cv2,os
cd =  os.getcwd()
resim_yolu = os.path.join(cd,"numpy","test.png")
image = cv2.imread(resim_yolu)
image_cut = image[0:250,600:800,:]
cv2.imshow("resim",image_cut)
cv2.waitKey(0)
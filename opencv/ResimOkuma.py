from cv2 import imread, waitKey, imshow, line, rectangle
import numpy as np
from os import getcwd, path
cd=getcwd()
impath=path.join(getcwd(),"opencv","images","road.jpg")
image=imread(impath)#Tipi nparray, uint8
imshow("Yol",image)
waitKey(0)


#1/4 Küçültme
image1=np.copy(image[::4,::4,:])
imshow("Yol Küçük",image1)
waitKey(0)
shape=image.shape
h=shape[0]
w=shape[1]
print(f"Resim'in Boyutu: {w}x{h}")

"""En Ortadaki Pikselin Renk Bilgisi"""
ilkrnk=image[0,0]
print(ilkrnk)


#bir grup pikseli değiştirme
image2=np.copy(image)
image2[0:100,0:100]=ilkrnk
imshow("Yol Boyalı",image2)
waitKey(0)


#Çizgi
image3=np.copy(image)
start=(w//2,h//2)
end=(w,h)
renk=(0,0,255)#BGR
kalinlik=4
line(image3,start,end,renk,kalinlik)
imshow("Yol Çizgili",image3[::2,::2])#1/2
waitKey(0)


#Dikdörtgen
image4=np.copy(image)
rectangle(image4,start,end,renk,kalinlik)
imshow("Yol Dikgörtgenli",image4[::2,::2])#1/2
waitKey(0)



"""YENİ RESİM"""""""""""""""""""""""""""""""""""""""""""""""""""
cd=getcwd()
impath=path.join(getcwd(),"opencv","images","chp1","marsrover.png")
from cv2 import imread, imshow, waitKey
from os import getcwd, path
import numpy as np
cd=getcwd()
impath=path.join(getcwd(),"opencv","images","yolResmi.jpg")
image=imread(impath)#Tipi nparray
#image=image[::4,::4,:]#1/4 Küçültme
shape=image.shape
h=shape[0]
w=shape[1]
print(f"Resim'in Boyutu: {w}x{h}")
imshow("Yol",image)
waitKey(0)

"""En Ortadaki Pikselin Renk Bilgisi"""
ilkrnk=image[0,0]
print(ilkrnk)
#bir grup pikseli değiştirme
image[0:100,0:100]=ilkrnk
imshow("Yol",image)
waitKey(0)
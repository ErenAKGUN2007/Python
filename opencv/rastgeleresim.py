
#rastgele resim
import cv2
import numpy as np
image=np.random.randint(0,255,size=(600,600,3),dtype=np.uint8)#tek renk için size son değeri 1 olmalı
cv2.imshow("Rastgele",image)
cv2.waitKey(0)

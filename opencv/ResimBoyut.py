from cv2 import *
from os import getcwd, path
import numpy as np
cd=getcwd()
ipath=path.join(cd,"opencv","images","chp2","zebra.png")
image=imread(ipath)

imshow("Zebra",image)
waitKey(0)

h,w,c=image.shape
aspect=w/h#en boy oranı
yenih=int(h*0.1)
yeniw=int(yenih*aspect)
dim=(yenih,yeniw)
image0_2=resize(image,dim,None)
imshow("Zebra 0,2",image0_2)
waitKey(0)

image0_4=resize(image,None,fx=0.4,fy=0.4,interpolation=INTER_AREA)
imshow("Zebra 0,4",image0_4)
waitKey(0)
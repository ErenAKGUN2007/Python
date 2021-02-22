from cv2 import *
import numpy as np
from os import *
cd=os.getcwd()
ipath=os.path.join(cd,"opencv","images","chp2","zebrasmall.png")
iorijinal=imread(ipath)
iorijinal=resize(iorijinal,None,fx=.5,fy=.5,interpolation=INTER_AREA)

imshow("Zebra 0.5",iorijinal)

h,w,c=iorijinal.shape

center1=(h//3,w//5)
angle1=45
scale1=1.0
rotateMatrix1=getRotationMatrix2D(center1,angle1,scale1)
image_rotate1=warpAffine(iorijinal,rotateMatrix1,(w,h))
imshow("Zebra Rotate1",image_rotate1)

center2=(h//2,w//5)
angle2=56
scale2=1.5
rotateMatrix2=getRotationMatrix2D(center2,angle2,scale2)
image_rotate2=warpAffine(iorijinal,rotateMatrix2,(w,h))
imshow("Zebra Rotate2",image_rotate2)

imageFlip_vert=flip(iorijinal,0) #Dikey 0, Yatay 1, Dikey+Yatay -1
imshow("Zebra Flip",imageFlip_vert)
waitKey(0)
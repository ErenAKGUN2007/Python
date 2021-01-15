from cv2 import *
from os import getcwd, path
import numpy as np
cd=getcwd()
ipath=path.join(cd,"opencv","images","chp2","soccer-in-green.jpg")
image=imread(ipath)
h,w,c=image.shape
dim=(h,w)
#dönüşüm matrisi
dm=np.float32([[1,0,50],[0,1,20]])#1.si yatay 2.si dikey(x,y pikselinden z piksel ilerlet)
imaget=warpAffine(image,dm,dim)
imshow("Top",image)
imshow("Top Dönüştürülmüş",imaget)
waitKey(0)
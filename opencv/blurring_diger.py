import cv2,os,numpy as np
impath=os.path.join(os.getcwd(),"opencv","images","chp2","park.jpg")

image=cv2.imread(impath)
cv2.imshow("Orijinal",image)

gaussianFiltering=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Gaussian5",gaussianFiltering)

bilateralFiltering=cv2.bilateralFilter(image,5,150,150)
cv2.imshow("Billateral5",bilateralFiltering)

cv2.waitKey(0)
import cv2,numpy as np,os
impath=os.path.join(os.getcwd(),"opencv","images","chp2","scanned_doc.png")#scanned_doc.png, sudoku.jpg, boat.jpg
image=cv2.imread(impath)
#image[0:100,0:100,:]=(250,20,20)
cv2.imshow("Orijinal",image)
print("image.shape: ",image.shape)
#gri
imgri=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri",imgri)
print("imgri.shape: ",imgri.shape)
#binarization(ikileştirme) (veriyi sadece iki şekilde ifade etme)
#thresold(eşikleme)
(T,imbinarized)=cv2.threshold(imgri,60,255,cv2.THRESH_BINARY)
cv2.imshow("Binarized",imbinarized)
print("imbinarized.shape: ",imbinarized.shape)
#thresold(eşikleme)_INV
(T,imbinarizedINV)=cv2.threshold(imgri,60,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Binarized_INV",imbinarizedINV)
print("imbinarizedINV.shape: ",imbinarizedINV.shape)

cv2.waitKey(0)
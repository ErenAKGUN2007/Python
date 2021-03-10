import cv2,numpy as np,os
impath=os.path.join(os.getcwd(),"opencv","images","chp2","scanned_doc.png")#scanned_doc.png, sudoku.jpg, boat.jpg
image=cv2.imread(impath)
cv2.imshow("Original",image)
#gri
imgri=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri",imgri)
#binarized
binarized=cv2.adaptiveThreshold(imgri,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,57,3)
cv2.imshow("Adaptive Binarized",binarized)

cv2.waitKey(0)
import cv2, numpy as np, os
impath=os.path.join(os.getcwd(),"opencv","images","chp2","sudoku.jpg")
image=cv2.imread(impath)
cv2.imshow("Orijinal",image)
imgri=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
imgri=cv2.bilateralFilter(imgri,5,50,50)

sobelx=cv2.Sobel(imgri,cv2.CV_64F,1,0,ksize=3)
#print(sobelx)
sobelx=np.uint8(np.absolute(sobelx))
#print(sobelx)
cv2.imshow("Sobel X",sobelx)

sobely=cv2.Sobel(imgri,cv2.CV_64F,0,1,ksize=3) #xy için 1,1 ama kötü
#print(sobely)
sobely=np.uint8(np.absolute(sobely))
#print(sobely)
cv2.imshow("Sobel Y",sobely)

#Laplace
laplace=cv2.Laplacian(imgri,cv2.CV_64F)
#print(laplace)
laplace=np.uint8(np.absolute(laplace))
#print(laplace)
cv2.imshow("Laplace",laplace)

#Canny
canny=cv2.Canny(imgri,30,170)
cv2.imshow("Canny",canny)

cv2.waitKey(0)
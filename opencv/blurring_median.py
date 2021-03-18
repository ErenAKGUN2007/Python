import cv2,os,numpy as np
impath=os.path.join(os.getcwd(),"opencv","images","chp2","salt-pepper.jpg")
image=cv2.imread(impath)
cv2.imshow("Orijinal",image)
blurred_im3=cv2.medianBlur(image,3)
cv2.imshow("Blurred3",blurred_im3)
blurred_im5=cv2.medianBlur(image,5)
cv2.imshow("Blurred5",blurred_im5)
blurred_im9=cv2.medianBlur(image,9)
cv2.imshow("Blurred9",blurred_im9)
blurred_im469=cv2.medianBlur(image,469)#max
cv2.imshow("Blurred469",blurred_im469)

cv2.waitKey(0)
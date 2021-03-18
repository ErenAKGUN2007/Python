import os, cv2, numpy as np
impath=os.path.join(os.getcwd(),"opencv","images","chp2","elmalar.jpg")#sekil_geo.jpg elmalar.jpg
imageO=cv2.imread(impath)
cv2.imshow("Orijinal",imageO)
image=cv2.medianBlur(imageO,15)
imgri=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,sbResim=cv2.threshold(imgri,220,255,cv2.THRESH_BINARY)
konturlar,_=cv2.findContours(sbResim,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(konturlar,len(konturlar))

#center=(konturlar[0][1][0][0],konturlar[0][1][0][1])
#cv2.circle(image,center,5,(0,0,255),-1)

for knt in konturlar:
    deger=cv2.approxPolyDP(knt,0.009*cv2.arcLength(knt,True),True)
    cv2.drawContours(imageO,[deger],0,(0,255,0),2)
cv2.imshow("Konturlu Resim",imageO)
#cv2.imshow("Konturlu Resi",sbResim)
print(len(konturlar))
cv2.waitKey(0)
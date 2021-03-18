import cv2, numpy as np
cap=cv2.VideoCapture(0)
ret,frame1=cap.read()
ret,frame2=cap.read()
while cap.isOpened():
    fark=cv2.absdiff(frame1,frame2)
    gri=cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    yumusak=cv2.GaussianBlur(gri,(5,5),0)
    t,sbResim=cv2.threshold(yumusak,20,255,cv2.THRESH_BINARY)
    yayilmis=cv2.dilate(sbResim,None,iterations=3)
    konturlar,_=cv2.findContours(yayilmis,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for knt in konturlar:
        x,y,w,h=cv2.boundingRect(knt)
        #print(cv2.contourArea(knt))
        if cv2.contourArea(knt)<1000:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(215,120,0),2)
        cv2.putText(frame1,"Hareket Tespit Edildi",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(215,120,0),3)

    #ret,frame1=cap.read()

    cv2.imshow("Kamera",frame1)
    cv2.imshow("Fark",fark)
    #cv2.imshow("Gri Fark",gri)
    #cv2.imshow("Gri Fark Yumuşak",yumusak)
    #cv2.imshow("Gri Fark Yumuşak Thresold",sbResim)
    cv2.imshow("Gri Fark Yumuşak Thresold Dilate",yayilmis)
    frame1=frame2
    ret,frame2=cap.read()
    if cv2.waitKey(40)==27:
        break
cv2.destroyAllWindows()
cap.release()
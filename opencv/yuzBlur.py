from cv2 import *
from os import path, getcwd
haar_path=path.join(getcwd(),"opencv","haarcascade_frontalface_alt.xml")
face_cascade=CascadeClassifier(haar_path)
cam=VideoCapture(0)
_,frame=cam.read()
while cam.isOpened():
    gri=cvtColor(frame,COLOR_BGR2GRAY)
    for (x,y,w,h) in face_cascade.detectMultiScale(gri,1.3,5):
        frame[y:y+h,x:x+w]=GaussianBlur(frame[y:y+h,x:x+w],(109,109),0)
    imshow("Kamera",frame)
    _,frame=cam.read()
    if waitKey(40)==27:
        break
destroyAllWindows()
cam.release()
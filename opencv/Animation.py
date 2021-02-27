import cv2
import numpy as np
import os
import  sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
import time
class App(QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.cd=os.getcwd()
        self.ui_path=os.path.join(self.cd,"opencv","animation.ui")
        self.InitUI()
        self.pencereAcık=True
    def InitUI(self):
        self.win=uic.loadUi(self.ui_path,self)
        #Olayları Bağlama
        self.win.btnTikla.clicked.connect(self.tiklandi)
        self.win.show()
    def closeEvent(self):
        self.pencereAcık=False
    def tiklandi(self):
        #print("Tıklandı")
        ipath=os.path.join(self.cd,"opencv","images","chp2","zebrasmall.png")
        image=cv2.imread(ipath)
        h,w,c=image.shape
        center=(w//2,h//2)
        angle=0
        scale=1.0
        while self.pencereAcık:
            rotation_matrix=cv2.getRotationMatrix2D(center,angle,scale)
            image_r=cv2.warpAffine(image,rotation_matrix,(w,h))
            angle+=5
            img=QImage(image_r.data,w,h,c*w,QImage.Format_RGB888)
            self.win.lblCam.setPixmap(QPixmap.fromImage(img))
            time.sleep(0.016)
            cv2.waitKey(0)
if __name__=="__main__":
    app=QApplication(sys.argv)
    uygulama=App()
    sys.exit(app.exec_())
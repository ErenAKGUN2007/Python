import numpy as np
from os import getcwd, path
from cv2 import imshow, waitKey, rectangle, circle, imwrite
cd=getcwd()
c_path=path.join(cd,"opencv","images","Daire.jpg")
r_path=path.join(cd,"opencv","images","Dikdörtgen.jpg")
o_path=path.join(cd,"opencv","images","Siyah.jpg")
canvasR=np.zeros((200,200,3),dtype=np.uint8)
canvasC=canvasR.copy()
canvasO=canvasR.copy()
waitKey(0)
start=(0,0)
end=(100,100)
c_center=(100,100)
radius=50
c_c=(255,0,0)
c_r=(255,255,0)
tknss=2
rectangle(canvasR,start,end,c_r,tknss)
circle(canvasC,c_center,radius,c_c,tknss)
imshow("Siyah",canvasO)
imshow("Siyah Dikdörtgen",canvasR)
imshow("Siyah Daire",canvasC)
waitKey(0)
imwrite(r_path,canvasR)
imwrite(c_path,canvasC)
imwrite(o_path,canvasO)
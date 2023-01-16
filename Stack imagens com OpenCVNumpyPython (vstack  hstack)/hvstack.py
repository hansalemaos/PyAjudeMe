# pip install cv2-multistack
from cv2_multistack import (
hstack_multiple_pics,
vstack_multiple_pics
)
import cv2
import glob
folder=r'C:\pics\picstobw'
listofpics = (
    glob.glob(folder + '\\*.png')
)
horizontal= vstack_multiple_pics(
    listofpics,
    width=300,
    channels=3
)
cv2.imwrite('c:\\vstackpics.png',
            horizontal)
#https://raw.githubusercontent.com/hansalemaos/screenshots/main/tensorflowscreen.png
image = r"F:\neuedownloads\tensorflowscreen.png"
co=(160, 159, 154)

from locate_pixelcolor import (
search_colors
)
import cv2
img = cv2.imread(image)
print(
    search_colors(
        pic=img,
        colors=[
            tuple(reversed(co))
        ]
    )
)




from PIL import Image
img = Image.open(image)
img = img.convert('RGB')
da = img.getdata()

def p():
    d=[]
    for i in da:
        if (i[0] == co[0] and
            i[1] == co[1] and
            i[2] == co[2]
        ):
            d.append(i)
    return d
print(p())
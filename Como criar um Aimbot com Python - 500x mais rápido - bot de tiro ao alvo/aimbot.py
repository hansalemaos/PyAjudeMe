# video: https://www.youtube.com/watch?v=g-3UujN5ERU
import mss # pip install mss
import numpy as np # pip install numpy
import cv2 #pip install opencv-python
from locate_pixelcolor import search_colors #pip install locate-pixelcolor
from mousekey import MouseKey # pip install mousekey
import keyboard
ativo = False

def on_off():
    global ativo
    ativo = not ativo
keyboard.add_hotkey('ctrl+alt+k', on_off)
mkey = MouseKey()
mkey.enable_failsafekill('ctrl+e')
c = 660,371,1240,790
rgb = 255,219,195
colors = tuple(reversed(rgb))
while True:
    if not ativo:
        continue
    with mss.mss() as sct:
        shot = np.array(sct.grab(sct.monitors[1]))
        shot = shot[c[1]:c[3], c[0]:c[2]]
        shot = cv2.cvtColor(
            shot, cv2.COLOR_RGBA2RGB
        )
        colfound = search_colors(
            pic=shot,
            colors=[colors]
        )
        coo=np.where(np.abs(
            np.diff(colfound[..., 0],
            prepend=0)) > 30)[0]
        [mkey.left_click_xy(x+c[0],y+c[1], delay=0.05)
         for x,y in colfound[coo]]


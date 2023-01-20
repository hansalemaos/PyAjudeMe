#https://youtu.be/UDe9LUn_Z3s
#https://www.roblox.com/games/8916037983/starving-artists-DONATION-GAME
from math import floor
from time import sleep
import cv2, mss #pip install mss
from a_cv2_shape_finder import get_shapes_using_THRESH_OTSU
import numpy as np
from PrettyColorPrinter import add_printer
from ctypes_rgb_values import get_pixel, rgba
from mousekey import MouseKey
from a_cv_imwrite_imread_plus import add_imwrite_plus_imread_plus_to_cv2
from a_cv2_easy_resize import add_easy_resize_to_cv2
rgb2hex = lambda r, g, b: "#%02x%02x%02x" % (r, g, b)


getpcor = lambda x,y:rgba(get_pixel
                (int(x),int(y)))[:-1]
add_imwrite_plus_imread_plus_to_cv2()
add_easy_resize_to_cv2()
add_printer(True)
imagepath = r'C:\Users\Gamer\Pictures\2023-01-19 20_19_36-mona lisa - Google Search.png'
im = cv2.imread_plus(imagepath, channels_in_output=3)
im1 = cv2.easy_resize_image(
    im.copy(), width=32, height=32,
    percent=None
)

pic3 = np.fliplr(im1)
pic3 = cv2.rotate(pic3, cv2.ROTATE_90_CLOCKWISE)
pic3 = cv2.rotate(pic3, cv2.ROTATE_180)

mkey = MouseKey()
mkey.enable_failsafekill('ctrl+e')
with mss.mss() as sct:
    shot = np.array(sct.grab(sct.monitors[1]))
    df, bw_pic = get_shapes_using_THRESH_OTSU(
        im=shot.copy(),
        method=cv2.CHAIN_APPROX_SIMPLE,
        approxPolyDPvar=0.01,
        kernel=(1, 1),
        start_thresh=50,
        end_thresh=255,
        return_bw_pic=True,
    )

df1=(df.loc[(df.aa_shape == 'square')]
.sort_values(by='aa_area', ascending=False)
).iloc[:1]

#cv2.imwrite_plus('f:\\bw_pic.png',bw_pic)

offsetx,offsety=(df1
    [['aa_bound_start_x', 'aa_bound_start_y']]
    .__array__().tolist()[0])

offi = floor(df1.aa_bound_width.iloc[0] / 32)

offsetx,offsety = (
    floor(offsetx + offi/2),
    floor(offsety + offi/2)
)

rainbowbuttonx = (
        int(df1.aa_bound_width.iloc[0]/7*5)
        +offsetx-10)

rainbowbuttony = offsety+50+df1.aa_bound_height.iloc[0]

entertextx = rainbowbuttonx
entertexty = rainbowbuttony - 90
corvermelhobagulho = (210, 76, 71)
check_red_color_x = entertextx - 250
check_red_color_y = int(entertexty)
sleep(5)
for offsetadd, y in enumerate(range(pic3.shape[0])):
    addtoy = offsetadd * offi
    for offsetaddx, x in enumerate(range(pic3.shape[1])):
        try:
            addtox = offsetaddx * offi
            colortodraw = tuple([int(b) for b in reversed(pic3[x, y].
                                                          tolist())])
            writecolor = rgb2hex(*colortodraw)[1:]

            while getpcor(check_red_color_x,
                          check_red_color_y) != corvermelhobagulho:
                try:
                    mkey.left_click_xy_natural(int(rainbowbuttonx),
                                               int(rainbowbuttony) )
                    sleep(.1)
                except Exception as uu:
                    print(uu)
                    continue
            sleep(.2)
            mkey.left_click_xy_natural(int(entertextx), int(entertexty) )
            sleep(.05)
            mkey.send_unicode(str(writecolor))
            sleep(.05)
            mkey.press_key('enter')
            sleep(.05)
            mkey.left_click_xy_natural(int(rainbowbuttonx), int(rainbowbuttony))
            cx = int(x//2 + offsetx + addtox)
            cy = int(y//2 + offsety + addtoy)
            co = (-1,-1,-1)
            counter = 0
            while co!=colortodraw:
                try:
                    mkey.left_click_xy_natural(cx,cy,delay=0.02)
                    sleep(.05)
                    co = getpcor(cx,cy)
                    sleep(.05)
                    if co==colortodraw:
                        break
                    mkey.left_click_xy_natural(cx-2, cy, delay=0.02)
                    sleep(.05)
                    co = getpcor(cx-2,cy)
                    sleep(.05)
                except Exception as baba:
                    print(baba)
                    continue
                if counter > 2:
                    break
                counter += 1
        except Exception as fe:
            print(fe)
            continue
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# clique = False
# if clique:
#     while getpcor(check_red_color_x,
#                   check_red_color_y) != corvermelhobagulho:
#
#
#         mkey.left_click_xy_natural(
#             rainbowbuttonx,
#             rainbowbuttony,)
#         sleep(.5)
#
#     mkey.left_click_xy_natural(
#         entertextx,
#         entertexty,)
#     sleep(.2)
#     mkey.send_unicode('#ff00ff')
#     sleep(.2)
#     mkey.press_key('enter')
#     sleep(.2)
#     mkey.left_click_xy_natural(
#         rainbowbuttonx,
#         rainbowbuttony,)















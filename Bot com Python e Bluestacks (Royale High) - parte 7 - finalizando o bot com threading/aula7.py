#https://youtu.be/-pOyiRRW8gg
import threading
from random import randrange
from time import sleep

from adbkit import ADBTools
import pandas as pd
from a_pandas_ex_image_tools import pd_add_image_tools

pd_add_image_tools()
from group_and_iter_everything import group_coordinates_by_distance
import numpy as np

adb_path = "C:\\Users\\Gamer\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe"
deviceserial = "localhost:5855"
adb = ADBTools(adb_path=adb_path, deviceserial=deviceserial)
adb.aa_connect_to_device()
adb.aa_root_bluestacks_instances()
adb.aa_enable_root()
adb.aa_activate_sendevent_touch()
adb.aa_activate_sendevent_keyboard(
    sdcard="/storage/emulated/0/",
    tmp_folder_on_sd_card="AUTOMAT",
    exit_keys="ctrl+x",
)
cores = [
    (44, 22, 89),
    (40, 30, 101),
    (43, 26, 100),
    (36, 34, 109),
    (35, 39, 113),
    (44, 24, 92),
    (44, 23, 90),
    (74, 86, 210),
    (52, 27, 108),
    (52, 28, 110),
    (44, 24, 93),
    (78, 92, 220),
    (39, 39, 113),
    (52, 28, 112),
    (69, 80, 199),
    (41, 41, 123),
    (45, 26, 97),
    (42, 43, 125),
    (46, 24, 96),
    (46, 26, 100),
    (45, 24, 94),
    (50, 35, 117),
    (44, 25, 93),
    (38, 32, 105),
    (47, 25, 99),
    (44, 23, 91),
    (52, 27, 106),
    (36, 36, 111),
    (44, 24, 95),
    (46, 25, 97),
    (41, 29, 101),
    (35, 43, 124),
    (37, 33, 107),
    (93, 42, 155),
    (114, 140, 255),
    (39, 31, 103),
    (43, 26, 96),
    (35, 43, 117),
    (64, 33, 127),
    (41, 28, 99),
    (41, 28, 100),
    (46, 29, 105),
    (116, 48, 180),
    (55, 31, 118),
    (55, 31, 114),
    (45, 27, 99),
    (41, 29, 100),
    (73, 36, 136),
    (188, 89, 240),
    (32, 42, 121),
    (43, 51, 143),
    (50, 66, 165),
    (50, 26, 101),
    (80, 37, 141),
    (52, 31, 112),
    (43, 43, 125),
    (52, 60, 159),
    (113, 146, 253),
    (43, 43, 130),
    (50, 35, 116),
    (50, 34, 118),
    (52, 28, 111),
    (42, 44, 126),
    (53, 29, 113),
    (88, 40, 151),
    (43, 43, 134),
    (53, 30, 114),
    (46, 23, 93),
    (87, 97, 233),
    (42, 27, 98),
    (50, 58, 157),
    (77, 36, 137),
    (76, 37, 139),
    (33, 40, 114),
    (74, 36, 137),
    (50, 26, 103),
    (71, 36, 133),
    (105, 130, 253),
    (49, 28, 105),
    (44, 25, 94),
    (71, 35, 133),
    (47, 30, 107),
    (48, 36, 118),
    (47, 31, 106),
    (51, 68, 167),
    (45, 25, 96),
    (35, 43, 125),
    (35, 41, 115),
    (35, 40, 113),
    (83, 99, 234),
    (35, 36, 111),
    (51, 26, 105),
    (62, 34, 125),
    (34, 51, 137),
    (34, 49, 134),
    (45, 23, 91),
    (51, 26, 106),
    (51, 27, 107),
    (232, 101, 254),
    (48, 26, 102),
    (34, 41, 117),
    (33, 45, 123),
    (33, 42, 119),
    (66, 34, 130),
    (35, 48, 131),
    (36, 35, 109),
    (47, 26, 101),
    (44, 24, 91),
    (92, 108, 247),
    (70, 83, 203),
    (49, 26, 103),
    (69, 81, 199),
    (39, 31, 104),
    (39, 30, 102),
    (57, 32, 118),
    (52, 26, 105),
    (47, 24, 95),
    (44, 24, 96),
    (38, 32, 106),
    (48, 25, 99),
    (207, 118, 251),
    (44, 24, 97),
    (47, 27, 103),
    (47, 28, 102),
    (45, 26, 100),
    (36, 49, 136),
    (67, 35, 129),
    (47, 29, 104),
    (95, 119, 253),
]
lock = threading.Lock()
def go_to_sleep():
    t=threading.Timer(randrange(600,1200), go_to_sleep)
    t.start()
    try:
        lock.acquire()
        adb.bb_sendevent_keyboard.press_dev_input_event0_r(1)
        lock.release()
        sleep(15)
        lock.acquire()
        adb.bb_sendevent_keyboard.press_dev_input_event0_key_space(1)
    finally:
        lock.release()

def wakeup():
    t=threading.Timer(randrange(30,90), wakeup)
    t.start()
    lock.acquire()
    try:
        adb.bb_sendevent_keyboard.press_dev_input_event0_key_space(1)
    finally:
        lock.release()

go_to_sleep()
wakeup()

while True:
    try:
        adb.aa_update_screenshot()
        df = pd.Q_image2df(adb.screenshot)
        dfm = df.im_multicolor_lookup(cores)
        color_groups = group_coordinates_by_distance(
            list(
                dfm[["x", "y"]].ds_to_tuples(
                    index=False,
                    columns=False,
                )
            ),
            limit_x=20,
            limit_y=20,
            continue_on_exceptions=True,
        )
        for color_group in color_groups:
            try:
                if len(color_group) < 20:
                    continue
                meanx = int(np.array(color_group)[..., 0].mean())
                meany = int(np.array(color_group)[..., 1].mean())
                print(meanx, meany)
                adb.bb_sendevent_touch.touch(meanx, meany)
            except Exception as fa:
                print(fa)
            sleep(.5)
        sleep(1)
    except Exception as fe:
        print(fe)
        continue

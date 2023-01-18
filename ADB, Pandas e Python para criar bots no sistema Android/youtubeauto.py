from adbkit import ADBTools
from locate_pixelcolor import search_colors
import numpy as np
import pandas as pd

adb_path = "C:\\Users\\Gamer\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe"
deviceserial = "localhost:5735"
adb = ADBTools(adb_path=adb_path, deviceserial=deviceserial)
adb.aa_connect_to_device()
adb.aa_disable_root()

adb.aa_update_screenshot()
uidf = lambda: (
    adb.aa_get_all_displayed_items_from_uiautomator(
        screenshotfolder="f:\\adrobot3",  # screenshots will be saved here
        max_variation_percent_x=10,  # used for one of the click functions, to not click exactly in the center - more information below
        max_variation_percent_y=10,  # used for one of the click functions, to not click exactly in the center
        loung_touch_delay=(
            1000,
            1500,
        ),  # with this settings longtouch will take somewhere between 1 and 1,5 seconds
        swipe_variation_startx=10,  # swipe coordinate variations in percent
        swipe_variation_endx=10,
        swipe_variation_starty=10,
        swipe_variation_endy=10,
        sdcard="/storage/emulated/0/",  # sdcard will be used if you use the sendevent methods, don't pass a symlink - more information below
        tmp_folder_on_sd_card="AUTOMAT",  # this folder will be created in the sdcard folder for using sendevent actions
        bluestacks_divider=32767,  # coordinates must be recalculated for BlueStacks https://stackoverflow.com/a/73733261/15096247 when using sendevent
        with_screenshot=True,
    )
)
df = uidf()


aidf = lambda: (
    adb.aa_get_all_displayed_items_from_activities(
        screenshotfolder="f:\\adrobot3",  # screenshots will be saved here
        max_variation_percent_x=10,  # used for one of the click functions, to not click exactly in the center - more information below
        max_variation_percent_y=10,  # used for one of the click functions, to not click exactly in the center
        loung_touch_delay=(
            1000,
            1500,
        ),  # with this settings longtouch will take somewhere between 1 and 1,5 seconds
        swipe_variation_startx=10,  # swipe coordinate variations in percent
        swipe_variation_endx=10,
        swipe_variation_starty=10,
        swipe_variation_endy=10,
        sdcard="/storage/emulated/0/",  # sdcard will be used if you use the sendevent methods, don't pass a symlink - more information below
        tmp_folder_on_sd_card="AUTOMAT",  # this folder will be created in the sdcard folder for using sendevent actions
        bluestacks_divider=32767,  # coordinates must be recalculated for BlueStacks https://stackoverflow.com/a/73733261/15096247 when using sendevent
    )
)

dfrapido = adb.aa_get_activity_execution_df_from_one_package(
        packagename='com.google.android.youtube'
    )
(
dfrapido.com_google_android_youtube_com_google_android_apps_youtube_app_application_Shell_UploadActivity__UPLOAD__DEFAULT__video.call(
    '-d file:///storage/emulated/0/DCIM/VID_20230117_213622.mp4')

)
from time import time, sleep
sleep(4)
df=uidf()
(df.loc[df.bb_text.str.contains(
'Titel erstellen', regex=False, na=False)]
.ff_bb_tap_center_variation.iloc[0]()
)

sleep(4)
adb.aa_activate_adb_keyboard()
adb.bb_adbkeyboard.activate_adb_keyboard()
sleep(2)
adb.bb_adbkeyboard.send_unicode_text_with_delay(
    ''.join(['àá'] * 2))

cinza = (214,215,215)

sleep(2)
adb.aa_update_screenshot()
df3 = aidf()
dfcoords = (df3.loc[df3.aa_class_name == 'android.widget.LinearLayout']
.dropna(subset='aa_screenshot')
['aa_screenshot'].apply(lambda x:
(search_colors(x, [(215,215,214)])))
)
dfcoords2 = dfcoords.apply(lambda x:pd.NA if not np.any(x
                            ) else x ).dropna()


dfcoords = dfcoords2.to_frame()
dfcoords['aa_min'] = dfcoords2.apply(lambda x: int(np.mean((x[...,0]))))
dfcoords3 = dfcoords.sort_values(by='aa_min').iloc[0].to_frame().T
dfcoords3=dfcoords3.rename(columns={'aa_min': 'aa_mean'})
dfcoords3 ['aa_mean2'] = dfcoords3.aa_screenshot.apply(

    lambda x: int(np.mean(x[...,1])))

dfclicar = df3.loc[dfcoords3.index[0]]
x_start = dfclicar.aa_cropped_x_start
y_start = dfclicar.aa_cropped_y_start

x_start = x_start+dfcoords3.aa_mean.iloc[0]
y_start = y_start+dfcoords3.aa_mean2.iloc[0]


adb.aa_execute_multiple_adb_shell_commands(
    f'input tap {x_start} {y_start}'
)


# adb.bb_adbkeyboard.disable_adb_keyboard()

# dfcoords2['aa_min'] = (
#     dfcoords2.apply(lambda x: int(np.mean((x[...,0])))))



# df3=aidf()
#
# # clicar no icone de YouTube
# (df.loc[(df.bb_class == 'android.view.View') &
# (df.bb_long_clickable) & (df.bb_index == 7)]
#
# ).ff_bb_tap_center_variation.iloc[0]()
#
#
# adb.aa_update_screenshot()
# from time import time, sleep
#
# timeout = 10
# timeout_final = time() + timeout
# start = time()
# while timeout_final > start:
#     df=uidf()
#     if df.empty:
#         continue
#     dfplus =(df.loc[(df.bb_class == 'android.widget.ImageView' ) &
#            (df.bb_content_desc.str.contains(r'^\s*$')) &
#            (df.bb_area > 600 ) &
#            (df.bb_resource_id == 'com.google.android.youtube:id/image')]
#             )
#     if not dfplus.empty:
#         dfplus.ff_bb_tap_center_variation.iloc[0]()
#         break
# adb.aa_update_screenshot()
# df=uidf()
#
# sleep(5)
# (df.loc[df.bb_pure_id == 'id/image']
# .sort_values(by='bb_center_x')
# ).ff_bb_tap_center_variation.iloc[0]()
#
# sleep(5)
# adb.aa_update_screenshot()
# df=uidf()
#
# df.loc[df.bb_content_desc == 'VID_20230117_213622.mp4'].ff_bb_tap_center_variation.iloc[0]()
#
#
#
# dfrapido = adb.aa_get_activity_execution_df_from_one_package(
#         packagename='com.google.android.youtube'
#     )









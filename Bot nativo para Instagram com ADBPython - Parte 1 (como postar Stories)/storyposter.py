from adbkit import ADBTools
from deviceid import deviceserial
from a_cv2_imshow_thread import add_imshow_thread_to_cv2
add_imshow_thread_to_cv2()
import cv2
adb_path =r'C:\ProgramData\chocolatey\bin\adb.exe'
dev = ADBTools(adb_path=adb_path, deviceserial=deviceserial)
dev.aa_connect_to_device()
_=dev.aa_update_screenshot()
# todas as atividades que podemos executar
dfa=dev.aa_get_activity_execution_df_from_one_package(
packagename="com.instagram.android")
# commando para subir um video nos stories (talvez seja diferente no seu)
dfa.com_instagram_android_com_instagram_share_handleractivity_CustomStoryShareHandlerActivity__ADD_TO_STORY__DEFAULT.call('-t "video" -d file:///storage/emulated/0/pali.m4v')
# imprimir o dataframe:
dfa.T.ds_color_print_all()

# atualizar o screenshot
dev.aa_update_screenshot()

# gerar um DataFrame com todos os elementos na tela
df=dev.aa_get_all_displayed_items_from_uiautomator(
	screenshotfolder="c:\\compare_android2",  # screenshots will be saved here
	max_variation_percent_x=4,  # used for one of the click functions, to not click exactly in the center - more information below
	max_variation_percent_y=4,  # used for one of the click functions, to not click exactly in the center
	loung_touch_delay=(
		1000,
		1500,
	),  # with this settings longtouch will take somewhere between 1 and 1,5 seconds
	swipe_variation_startx=10,  # swipe coordinate variations in percent
	swipe_variation_endx=10,
	swipe_variation_starty=10,
	swipe_variation_endy=10,
	sdcard="/sdcard/",  # sdcard will be used if you use the sendevent methods, don't pass a symlink - more information below
	tmp_folder_on_sd_card="AUTOMAT",  # this folder will be created in the sdcard folder for using sendevent actions
	bluestacks_divider=32767,  # coordinates must be recalculated for BlueStacks https://stackoverflow.com/a/73733261/15096247 when using sendevent
)

# salvar os screenshots:
df.ff_bb_save_screenshot.dropna().apply(lambda k:k())

df1=df.loc[df.bb_content_desc == 'Share to']
df1.ff_bb_tap_exact_center.iloc[0]()

# clicar num item
df1.ff_bb_tap_exact_center.iloc[0]()
df1.ff_bb_tap_center_offset(0,20)

# alguns exemplos de df.loc
df.loc[df.bb_class == 'android.widget.FrameLayout']
df.loc[df.bb_content_desc == 'Share to']
df.loc[df.bb_pure_id == 'id/share_story_button']

# funcao para facilitar
def get_update():
    dev.aa_update_screenshot()
    df = dev.aa_get_all_displayed_items_from_uiautomator(
        screenshotfolder="c:\\compare_android2",  # screenshots will be saved here
        max_variation_percent_x=4,
        # used for one of the click functions, to not click exactly in the center - more information below
        max_variation_percent_y=4,  # used for one of the click functions, to not click exactly in the center
        loung_touch_delay=(
            1000,
            1500,
        ),  # with this settings longtouch will take somewhere between 1 and 1,5 seconds
        swipe_variation_startx=10,  # swipe coordinate variations in percent
        swipe_variation_endx=10,
        swipe_variation_starty=10,
        swipe_variation_endy=10,
        sdcard="/sdcard/",
        # sdcard will be used if you use the sendevent methods, don't pass a symlink - more information below
        tmp_folder_on_sd_card="AUTOMAT",  # this folder will be created in the sdcard folder for using sendevent actions
        bluestacks_divider=32767,
        # coordinates must be recalculated for BlueStacks https://stackoverflow.com/a/73733261/15096247 when using sendevent
    )
    return df
df = get_update()
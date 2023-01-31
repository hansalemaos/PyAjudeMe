from pdwinauto import mkey, get_automation_frame_from_pid,get_automation_frame_from_all_pids,    click_on_main_menu,    click_on_submenu
from kthread_sleep import sleep
import sys
mkey.enable_failsafekill("ctrl+e")
gdf = lambda: get_automation_frame_from_pid(
    pids=[12132], uia=True,
    screenshot_folder='f:\\screenshotstestx1',
    timeout=30)
df=gdf()
text='oi, meu amigo!'
df=df.dropna(subset='aa_menu_items')
df.mm_send_unicode_force_activate.iloc[0](text)
n1='&File'
n2='&Save\tCtrl+S'
click_on_main_menu(df, menu1text=n1)
sleep(.5)
df2 = gdf()
click_on_submenu(df2.dropna(
subset="aa_menu_items"), menu1text=n1,
menu2text=n2,)
sleep(.5)
path = "F:\\tesa\\testxx3.txt"
while True:
    df33 = gdf()
    f1=df33.d_loc_no_exception('str.contains', '.txt')
    f2 = f1.loc[f1.aa_class_name == 'Edit']
    if not f2.empty:
        f2.iloc[0].mm_send_unicode_force_activate(path)
        break
sleep(1)
df55=gdf()
(df55.loc[df55.ff_CurrentDefaultAction == 'Save']
.iloc[0].ff_DoDefaultAction())

#df3 = get_automation_frame_from_all_pids(uia=True, screenshot_folder=None)

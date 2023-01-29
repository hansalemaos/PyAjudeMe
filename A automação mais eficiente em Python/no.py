from pdwinauto import (
   mkey,
   click_on_main_menu,
   click_on_submenu,
   get_automation_frame_from_pid,
   sleep
)
mkey.enable_failsafekill("ctrl+e")
n1,n2 = "&File","&Save\tCtrl+S"
filepath = "F:\\tesa\\testtext15.txt"
text = "Hallo, mein Freund, wie geht es dir?"
pid = 18596
gdf = lambda: get_automation_frame_from_pid(pid)
df = gdf()
df.mm_send_unicode_force_activate.iloc[0](text)
sleep(1)
df4 = df.dropna(subset="aa_menu_items")
click_on_main_menu(df4[:1], menu1text=n1)
sleep(1)
df2 = gdf()
click_on_submenu(df2.dropna(subset="aa_menu_items"
                           ), menu1text=n1, menu2text=n2)
while True:
   sleep(2)
   try:
       df = gdf()
       f1 = df.d_loc_no_exception("str.contains",r"\.txt",
                                  regex=True)
       f2 = f1.d_loc_no_exception("str.contains",r"Edit")
       f2.iloc[0].mm_send_unicode_force_activate(filepath)
       sleep(2)
       df.loc[df.ff_CurrentDefaultAction ==
              "Save"].iloc[0].ff_DoDefaultAction()
       sleep(1)
       (df.loc[~df.ff_Close.isna() &
              (df.aa_title == 'Notepad')]
        .iloc[0].ff_Close())
       break
   except Exception as fe:
       continue
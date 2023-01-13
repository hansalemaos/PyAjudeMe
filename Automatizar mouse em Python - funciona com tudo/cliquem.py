# pip install mousekey
import mousekey
import keyboard
ativo = False

def on_off():
    global ativo
    ativo = not ativo
keyboard.add_hotkey(
    'ctrl+alt+k',
    on_off
)

while True:
    if not ativo:
        continue
    mousekey.left_click(
        delay=0.005
    )
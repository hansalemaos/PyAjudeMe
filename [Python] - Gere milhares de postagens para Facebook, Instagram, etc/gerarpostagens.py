import os, glob, cv2
from random import choice
import cv2
import pandas as pd
from create_empty_image import create_new_image
from cv2_fit_text_in_box import fit_text_in_box
from cv2watermark import merge_image
from windows_filepath import make_filepath_windows_comp
from PrettyColorPrinter import add_printer

add_printer(True)
df = pd.read_excel(r"F:\opencvposts\a.xlsx")
df = (
    pd.concat([df, df.antworten.str.split("|", expand=True)], ignore_index=True, axis=1)
).drop(columns=2)
df.columns = range(df.shape[1])
pasta = r"F:\pasta_de_exercicios"
textcolors_alemao = [(255, 255, 0), (255, 0, 0)]
textcolors_portugues = [(80, 80, 0), (80, 0, 0)]
boxcolors_alemao = [(0, 0, 0)]
boxcolors_portugues = [(10, 10, 10)]
imagecolor = [(255, 255, 0), (255, 0, 0)]
folderpng = [
    cv2.imread(x, cv2.IMREAD_UNCHANGED)
    for x in glob.glob(r"F:\opencvposts\fotosvonmir\*.png")
]

for key, item in df[:3].iterrows():
    alemao = item[0]
    fp = make_filepath_windows_comp(
        filepath=alemao,
        fillvalue="_",  # replacement of any illegal char
        reduce_fillvalue=True,  # */<> (illegal chars) -> ____ (replacement) -> _ (reduced replacement)
        remove_backslash_and_col=True,  # important for multiple folders
        spaceforbidden=True,  # '\s' -> _
        other_to_replace=(
            "[",
            "]",
            "`",
            "=",
        ),  # other chars you don't want in the file path
        slash_to_backslash=False,  # replaces / with \\ before doing all the other replacements
    )

    fp = os.path.join(pasta, f"{fp}.png")
    portugues = item[1]
    resposta1 = f"A) {item[2]}"
    resposta2 = f"B) {item[3]}"
    resposta3 = f"C) {item[4]}"
    b = create_new_image(width=1000, height=1000, color=(255, *choice(imagecolor)))
    fertig = fit_text_in_box(
        alemao,
        textcolor=[choice(textcolors_alemao)],
        backgroundcolor=[choice(boxcolors_alemao)],
        transparent=True,
        filepath=fp,
        maximalx=850,
        maximaly=100,
        columns=1,
        fontart=r"C:\Windows\Fonts\ANTQUAB.TTF",
        fontborder=0,
        distance_upper_left=(0, 0),
    )
    b = merge_image(back=b, front=fertig, x=50, y=50, save_path=fp)
    fertig = fit_text_in_box(
        portugues,
        textcolor=[choice(textcolors_portugues)],
        backgroundcolor=[choice(boxcolors_portugues)],
        transparent=True,
        filepath=fp,
        maximalx=850,
        maximaly=100,
        columns=1,
        fontart=r"C:\Windows\Fonts\ANTQUAB.TTF",
        fontborder=0,
        distance_upper_left=(0, 0),
    )
    b = merge_image(back=b, front=fertig, x=50, y=200, save_path=fp)

    fertig = fit_text_in_box(
        f"{resposta1}\n{resposta2}\n{resposta3}",
        textcolor=[choice(textcolors_alemao)],
        backgroundcolor=[choice(boxcolors_alemao)],
        transparent=True,
        filepath=fp,
        maximalx=600,
        maximaly=400,
        columns=1,
        fontart=r"C:\Windows\Fonts\ANTQUAB.TTF",
        fontborder=10,
        distance_upper_left=(10, 10),
    )

    b = merge_image(back=b, front=fertig, x=50, y=400, save_path=fp)

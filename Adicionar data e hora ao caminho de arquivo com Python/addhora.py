from time import strftime
import os, pathlib


def st(path, last=True, sep="#"):
    p = pathlib.Path(path)
    sta = strftime("%Y_%m_%d_%H_%M_%S")
    fname = f"{sta}{sep}{p.stem}" if last else f"{p.stem}{sep}{sta}"
    fname += p.suffix
    return os.path.normpath(f"{os.sep}".join(list(p.parts[:-1] + (fname,))))


print(st("c:\\bax\\ii.jpg", last=True, sep="#"))
print(st("c:\\bax\\bu bu\\ii.jpg", last=True, sep="#"))
print(st("c:\\bax\\bu bu\\ii.jpg", last=False, sep="__"))
print(st("c:\\xa", last=False, sep="----"))
print(st("c:\\xa/tutu\\bax/bibi.xlsx", last=False, sep="oooooo"))
print(st("c:\\xa/tutu\\bax/bibi.xlsx", last=True, sep="@"))

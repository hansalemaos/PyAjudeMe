import os, shutil


def flatcopy(rdir, output, sep):
    allnewfiles = []
    if not os.path.exists(output):
        os.makedirs(output)
    for sdirs, dirs, files in os.walk(rdir):
        newfiles = [
            shutil.copyfile(
                g := os.path.join(sdirs, k),
                os.path.join(output, g.replace(os.sep, sep).replace(":", "")),
            )
            for k in files
        ]
        allnewfiles.extend(newfiles)
    return allnewfiles


flatcopy(rdir=r"C:\flc", output=r"C:\outputfolder", sep="#")

from PIL import Image
import os
imagepath = r"E:\zebras.jpeg"
outputfolder = r'E:\zebraconvert'
imageoriginal = Image.open(imagepath)
width = imageoriginal.size[0]
height = imageoriginal.size[1]
quality,steps,howmany = 100,100,10
filetype = 'jpg'
bestfilter = Image.Resampling.LANCZOS
for q in range(howmany):
    newwidth = width + (q*steps)
    percentage = newwidth/width
    newheight = int(height*percentage)
    newpath = os.path.join(
        outputfolder,
        f'{newwidth}x{newheight}.{filetype}'
    )
    imageoriginal.resize(
        (newwidth,newheight),bestfilter
    ).save(newpath,quality=quality)


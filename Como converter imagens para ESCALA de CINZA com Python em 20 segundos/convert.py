import cv2, glob

[
    cv2.imwrite(im, cv2.imread(im, cv2.IMREAD_GRAYSCALE))
    for im in glob.glob(r"C:\picstobw\*.png")
]

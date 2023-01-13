import cv2 # pip install opencv-python
from cv2watermark import merge_image_percentage_width_position # pip install cv2watermark
import glob
watermark = cv2.imread(r"C:\watermark.png", cv2.IMREAD_UNCHANGED)
watermark[..., 3] //= 2
imgs=[merge_image_percentage_width_position(
    back=cv2.imread(x),
    front=watermark,
    percentx=65,
    percenty=65,
    front_percentage_width=30,
    save_path=x.replace('.png', '_watermark.png',
)) for x in glob.glob(r'C:\Users\Gamer\Documents\Downloads\pics2\*.png')]
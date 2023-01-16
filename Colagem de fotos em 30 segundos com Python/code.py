import os

# pip install cv2-collage
from cv2_collage import create_collage

folder = r"C:\pics"

lst = [os.path.join(folder, file) for file in os.listdir(folder)]

collage = create_collage(
    lst=lst, width=1000, background=(0, 0, 0), save_path="c:\\collage_ready.png"
)

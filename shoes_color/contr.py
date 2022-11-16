import cv2
import numpy as np
from PIL import Image

img = Image.open("translated.png")
img4 = Image.open("background.png")
(img_h, img_w) = img.size
resize_back = img4.resize((img_h, img_w))

resize_back.paste(img,(0,0),img)
resize_back.show()
resize_back.save('shoe.png')
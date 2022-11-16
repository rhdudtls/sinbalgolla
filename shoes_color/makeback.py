import cv2
import numpy as np

img = cv2.imread('translated.png')
backg = np.full((img.shape[0], img.shape[1], 3), (15, 57, 0), dtype=np.uint8)
cv2.imwrite('background.png', backg)
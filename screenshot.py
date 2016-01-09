import numpy as np
from PIL import ImageGrab
import cv2
import pytesseract
from PIL import Image

printscreen_pil =  ImageGrab.grab(bbox=(760,575, 1255,920))
printscreen_numpy = np.array(printscreen_pil.getdata(), dtype='uint8').reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))

printscreen_numpy = cv2.cvtColor(printscreen_numpy, cv2.COLOR_BGR2GRAY)

cv2.imwrite("screencap.png", printscreen_numpy)

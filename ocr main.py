import numpy as np
from PIL import ImageGrab
import cv2
import pytesseract
from PIL import Image
#import enchant

#d = enchant.Dict("en_US")

ocr_guess = pytesseract.image_to_string(Image.open("screencap.png"))

words_ocr = ocr_guess.split(" ")

print " ".join(words_ocr)

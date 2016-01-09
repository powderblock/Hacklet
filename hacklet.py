import numpy as np
from PIL import ImageGrab
import cv2
import pytesseract
from PIL import Image

words = [["usurp", "seize", "seize and take control without authority"],
         ["moiety", "one of two basic subdivisions of a tribe"],
         ["portentous", "of momentous or ominous significance", "prophetic"],
         ["harbinger"],
         ["partisan"],
         ["hallowed"],
         ["auspicious"],
         ["filial"],
         ["obsequious"],
         ["retrograde"],
         ["jocund"],
         ["discourse"],
         ["truant"],
         ["countenance"],
         ["tenable"],
         ["besmirch"],
         ["prodigal"],
         ["libertine"],
         ["unfledged"],
         ["censure"],
         ["husbandry"],
         ["parley"],
         ["beguile"],
         ["traduce"],
         ["canonize"],
         ["sovereignty"],
         ["adulterate"],
         ["enmity"],
         ["pernicious"],
         ["antic"]]

from math import *
import sys
import re
import numpy as np
import cv2
import sys
from collections import *

def distance(a, b):
    return sqrt(sum((a - b) ** 2 for a, b in zip(a, b)))

def classify(a, dataset):
    distances = []
    for item in dataset:
        distances.append(((distance(a, item[0])), item[1]))
    return sorted(distances)[0][1]

images = []

classes = ["spell", "multi"]

for letter in classes:
    for i in range(6):
        print letter+"{0}.png".format(i)
        img = cv2.imread("classes/"+letter+"{0}.png".format(i))

        width = img.shape[0]
        height = img.shape[1]

        pixels = []

        # For every pixel in the image:
        for x in range(height):
            for y in range(width):
                red = img[y, x, 2]
                green = img[y, x, 1]
                blue = img[y, x, 0]
                if red == 255 and green == 255 and blue == 255:
                    pixels.append(1)
                else:
                    pixels.append(0)

        images.append((pixels, letter))

print images

def arrayOutput(img):
    img = cv2.imread(img)

    width = img.shape[0]
    height = img.shape[1]

    pixels = []

    # For every pixel in the image:
    for x in range(height):
        for y in range(width):
            red = img[y, x, 2]
            green = img[y, x, 1]
            blue = img[y, x, 0]
            if red == 255 and green == 255 and blue == 255:
                pixels.append(1)
            else:
                pixels.append(0)
    return pixels

print classify(arrayOutput("classify/spell_class.png"), images)


printscreen_pil =  ImageGrab.grab(bbox=(760,575, 1255,920))
printscreen_numpy = np.array(printscreen_pil.getdata(), dtype='uint8').reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))

printscreen_numpy = cv2.cvtColor(printscreen_numpy, cv2.COLOR_BGR2GRAY)

cv2.imwrite("screencap.png", printscreen_numpy)
#print pytesseract.image_to_string(Image.open("screencap.png"))

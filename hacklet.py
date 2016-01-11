import numpy as np
from PIL import ImageGrab
import cv2
import pytesseract
from PIL import Image
from math import *
import sys
import re
import sys
from collections import *

words = [["usurp", "seize", "seize and take control without authority"],
         ["moiety", "one of two basic subdivisions of a tribe"],
         ["portentous", "of momentous or ominous significance", "prophetic"],
         ["harbinger", "forerunner", "something indicating the approach of something or someone"],
         ["partisan", "a pike with a long tapering blade with lateral projections", "devoted to cause or party"],
         ["hallowed", "worthy of religious veneration", "religious groups", "holy"],
         ["auspicious", "auguring favorable circumstances and good luck"],
         ["filial", "relating to or characteristic of or befitting an offspring", "designating the generating following the parental generation"],
         ["obsequious", "attentive in an ingratiating or servile manner", "attempting to win favour from influential people by flattery"],
         ["retrograde", "moving or directed or tending in a backward direction"],
         ["jocund", "joyous", "merry", "full of or showing high-spirited merriment"],
         ["discourse", "debate", "extended verbal expression in speech or writing"],
         ["truant", "one who is absent from school without permission", "absent without permission"],
         ["countenance", "the appearance conveyed by a person's face", "visage"],
         ["tenable", "sensible", "based on sound reasoning or evidence"],
         ["besmirch", "a tabloid magazine", "smear so as to make dirty or stained"],
         ["prodigal", "recklessly wasteful", "wasteful"],
         ["libertine", "unrestrained by convention or morality", "a dissolute person", "debauched"],
         ["unfledged", "young and inexperienced", "inexperienced"],
         ["censure", "harsh criticism or disapproval", "reprimand"],
         ["husbandry", "the practice of cultivating the land or raising stock"],
         ["parley", "a negotiation between enemies"],
         ["beguile", "trick", "attract; cause to be enamored"],
         ["traduce", "slander", "speak unfavorably about", "defame"],
         ["canonize", "treat as a sacred person", "declare (a dead person) to be a saint"],
         ["sovereignty", "the authority of a state to govern another state", "royal authority; the dominion of a monarch", "government free from external control"],
         ["adulterate", "mixed with impurities"],
         ["enmity", "a state of deep-seated ill-will", "a scowl"],
         ["pernicious", "exceedingly harmful", "harmful"],
         ["antic", "a ludicrous or grotesque act done for fun and amusement", "ludicrously odd"]]

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
    for i in range(8):
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

printscreen_pil =  ImageGrab.grab(bbox=(760,575, 1255,920))
printscreen_numpy = np.array(printscreen_pil.getdata(), dtype='uint8').reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))

printscreen_numpy = cv2.cvtColor(printscreen_numpy, cv2.COLOR_BGR2GRAY)

cv2.imwrite("screencap.png", printscreen_numpy)
#print pytesseract.image_to_string(Image.open("screencap.png"))

print classify(arrayOutput("screencap.png"), images)

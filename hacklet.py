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

words = [["usurp", "seize", "seize and take control without authority", "assuming"],
         ["moiety", "one of two basic subdivisions of a tribe"],
         ["portentous", "of momentous or ominous significance", "prophetic"],
         ["harbinger", "forerunner", "something indicating the approach of something or someone", "precursor"],
         ["partisan", "a pike with a long tapering blade with lateral projections", "devoted to cause or party", "a fervent and even militant proponent of something"],
         ["hallowed", "worthy of religious veneration", "religious groups", "holy"],
         ["auspicious", "auguring favorable circumstances and good luck"],
         ["filial", "relating to or characteristic of or befitting an offspring", "designating the generating following the parental generation"],
         ["obsequious", "attentive in an ingratiating or servile manner", "attempting to win favour from influential people by flattery"],
         ["retrograde", "moving or directed or tending in a backward direction"],
         ["jocund", "joyous", "merry", "full of or showing high-spirited merriment", "at a New Year's celebration"],
         ["discourse", "debate", "extended verbal expression in speech or writing", "hold forth"],
         ["truant", "one who is absent from school without permission", "absent without permission"],
         ["countenance", "the appearance conveyed by a person's face", "visage"],
         ["tenable", "sensible", "based on sound reasoning or evidence"],
         ["besmirch", "a tabloid magazine", "smear so as to make dirty or stained", "denigrate"],
         ["prodigal", "recklessly wasteful", "wasteful"],
         ["libertine", "unrestrained by convention or morality", "a dissolute person", "debauched"],
         ["unfledged", "young and inexperienced", "inexperienced"],
         ["censure", "harsh criticism or disapproval", "reprimand", "rebuke formally"],
         ["husbandry", "the practice of cultivating the land or raising stock", "by helping to provide food", "farming"],
         ["parley", "a negotiation between enemies"],
         ["beguile", "trick", "attract; cause to be enamored", "fascinated", "enchant", "mesmerizes"],
         ["traduce", "slander", "speak unfavorably about", "defame", "denigrate"],
         ["canonize", "treat as sacred people", "treat as a sacred person", "declare (a dead person) to be a saint", "revere"],
         ["sovereignty", "the authority of a state to govern another state", "royal authority; the dominion of a monarch", "government free from external control"],
         ["adulterate", "mixed with impurities"],
         ["enmity", "a state of deep-seated ill-will", "a scowl", "the feeling of a hostile person"],
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

printscreen_pil =  ImageGrab.grab(bbox=(760, 575, 1255, 920))
printscreen_numpy = np.array(printscreen_pil.getdata(), dtype='uint8').reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))

printscreen_numpy = cv2.cvtColor(printscreen_numpy, cv2.COLOR_BGR2RGB)

cv2.imwrite("screencap.png", printscreen_numpy)
#print pytesseract.image_to_string(Image.open("screencap.png"))

def lookForWord():
    word = cv2.imread("screencap.png")

    width = word.shape[0]
    height = word.shape[1]

    # For every pixel in the image:
    for x in range(height):
        for y in range(width):
            red = word[y, x, 2]
            green = word[y, x, 1]
            blue = word[y, x, 0]
            if red > 40 and green > 40 and blue > 40:
                    word[y, x, 2] = 255
                    word[y, x, 1] = 255
                    word[y, x, 0] = 255
            else:
                word[y, x, 2] = 0
                word[y, x, 1] = 0
                word[y, x, 0] = 0
    cv2.imwrite("word.png", word)

def lookForAnswer():
    answers = cv2.imread("screencap.png")

    width = answers.shape[0]
    height = answers.shape[1]

    # For every pixel in the image:
    for x in range(height):
        for y in range(width):
            red = answers[y, x, 2]
            green = answers[y, x, 1]
            blue = answers[y, x, 0]
            if red == 105 and green == 170 and blue == 68:
                answerBlock = answers[y - 10:height, x - 5:width]
                cv2.imwrite("answers.png", answerBlock)
                return

def multipleChoice():
    lookForWord()
    lookForAnswer()

if(classify(arrayOutput("screencap.png"), images) == "multi"):
    multipleChoice()

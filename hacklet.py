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
import pytesseract

words = [["usurp", "assume", "take over", "seize", "seize and take control without authority", "assuming"],
         ["moiety", "one of two approximately equal parts", "one of two basic subdivisions of a tribe"],
         ["portentous", "ominously prophetic", "of momentous or ominous significance", "prophetic"],
         ["harbinger", "herald", "forerunner", "something indicating the approach of something or someone", "precursor"],
         ["partisan", "an enthusiastic supporter of some person or activity", "a pike with a long tapering blade with lateral projections", "devoted to cause or party", "a fervent and even militant proponent of something"],
         ["hallowed", "sacred", "worthy of religious veneration", "religious groups", "holy"],
         ["auspicious", "auguring favorable circumstances and good luck", "subservient" "auguring favorable circumstances and good luck"],
         ["filial", "daugterly", "relating to or characteristic of or befitting an offspring", "designating the generating following the parental generation"],
         ["obsequious", "attentive in an ingratiating or servile manner", "attempting to win favour from influential people by flattery"],
         ["retrograde", "going from better to worse", "moving or directed or tending in a backward direction"],
         ["jocund", "joyous", "merry", "full of or showing high-spirited merriment", "at a New Year's celebration"],
         ["discourse", "conversation", "talk at length and formally about a topic", "debate", "extended verbal expression in speech or writing", "hold forth"],
         ["truant", "absent", "someone who shriks duty" "one who is absent from school without permission", "absent without permission"],
         ["countenance", "prohibit", "face", "the appearance conveyed by a person's face", "visage"],
         ["tenable", "rational", "sensible", "based on sound reasoning or evidence"],
         ["besmirch", "cleanse", "a tabloid magazine", "smear so as to make dirty or stained", "denigrate"],
         ["prodigal", "gambling", "recklessly wasteful", "wasteful"],
         ["libertine", "debauchee", "immoral", "unrestrained by convention or morality", "a dissolute person", "debauched"],
         ["unfledged", "young and inexperienced", "inexperienced", "callow"],
         ["censure", "harsh criticism or disapproval", "reprimand", "rebuke formally"],
         ["husbandry", "the practice of cultivating the land or raising stock", "by helping to provide food", "farming"],
         ["parley", "discuss, as between enemies", "a negotiation between enemies"],
         ["beguile", "influence by slyness", "a flirtatious man charms everyone he meets", "trick", "attract; cause to be enamored", "fascinated", "enchant", "mesmerizes"],
         ["traduce", "disparage", "slander", "speak unfavorably about", "defame", "denigrate", "malign"],
         ["canonize", "revere", "treat as sacred people", "treat as a sacred person", "declare (a dead person) to be a saint", "revere"],
         ["sovereignty", "the authority of a state to govern another state", "royal authority; the dominion of a monarch", "government free from external control"],
         ["adulterate", "make impure by adding a foreign or inferior substance", "mixed with impurities"],
         ["enmity", "hostilities", "a state of deep-seated ill-will", "a scowl", "the feeling of a hostile person"],
         ["pernicious", "working or spreading in a hidden and usually injurious way", "exceedingly harmful", "harmful", "deadly"],
         ["antic", "joke", "a ludicrous or grotesque act done for fun and amusement", "ludicrously odd"]]

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
                answerBlock = answers[y - 10:width, x - 5:height]
                cv2.imwrite("answers.png", answerBlock)
                return

def multipleChoice():
    lookForWord()
    lookForAnswer()
    ocr_guess = pytesseract.image_to_string(Image.open("word.png"))

    words_ocr = ocr_guess.split("\n")
    answers_guess = pytesseract.image_to_string(Image.open("answers.png")).replace("0 ", "").replace("O ", "")

    answers_guess = answers_guess.split("\n")

    for word in words:
        if word[0] == words_ocr[0]:
            for answers in word:
                for answer in answers_guess:
                    if answers == answer:
                        print answer.index()

def lookForPlay():
    print "Look for play."

def spell():
    lookForPlay()

if(classify(arrayOutput("screencap.png"), images) == "multi"):
    multipleChoice()

else:
    spell()

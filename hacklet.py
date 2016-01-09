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

printscreen_pil =  ImageGrab.grab(bbox=(760,575, 1255,920))
printscreen_numpy = np.array(printscreen_pil.getdata(), dtype='uint8').reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))

printscreen_numpy = cv2.cvtColor(printscreen_numpy, cv2.COLOR_BGR2GRAY)

cv2.imwrite("screencap.png", printscreen_numpy)
print pytesseract.image_to_string(Image.open(printscreen_numpy))

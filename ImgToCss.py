import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()

Img = cv2.imread(filename)
Img = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)

Css = open("A.css",'w+')

Css.write(".Img\n{\nwidth: 1px;\nheight: 1px;\nbox-shadow:\n")

for i in range(len(Img)):
    for j in range(len(Img[0])):
        if i == len(Img)-1 and j == len(Img[0])-1:
            Css.write(str(j) + "px " + str(i) + "px rgb(" + str(Img[i][j][0])+ ',' + str(Img[i][j][1]) + ',' + str(Img[i][j][2]) + ");\n")
        else:
            Css.write(str(j) + "px " + str(i) + "px rgb(" + str(Img[i][j][0])+ ',' + str(Img[i][j][1]) + ',' + str(Img[i][j][2]) + "),\n")

Css.write("}")     
Css.close()

html = open("A.html",'w+')

html.write('<link rel="stylesheet" href="A.css">\n<div class="Img"></div>')
html.close()
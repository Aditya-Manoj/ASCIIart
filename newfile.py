# import tkinter as tk
from tkinter import Frame
import cv2
from PIL import Image, ImageDraw

filepath = r'E:\IMPORTANT ONLY\Python Projects\img2txt\ASCIIart\im3.jpg'
bstring = '@#W$9876543210?!abc;:+=-,._     '
stepsize = 7
blen = len(bstring)
den = 256/blen

original = cv2.imread(filepath)
original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
frame = cv2.imread(filepath, 0)
y = frame.shape[0]
x = frame.shape[1]

finaly = 100
finalx = int((100 * x) / y)
# finaly = y
# finalx = x
frame = cv2.resize(frame, (finalx, finaly))
original = cv2.resize(original, (finalx, finaly))

framesize = str(frame.shape[1]*stepsize) + 'x' + str(frame.shape[0]*stepsize)
print(framesize)

out = Image.new("RGB", (int(frame.shape[1]*stepsize), int(frame.shape[0]*stepsize)), (255, 255, 255))
d = ImageDraw.Draw(out)

# print(original[1][1])
for i in range(finaly):
    for j in range(finalx):
        fval = frame[i][j]
        bstrindex = int(fval//den)
        
        d.text((j*stepsize, i*stepsize), bstring[bstrindex], fill=tuple(original[i][j]))

out.show()
out.save("converted.png", format="png")
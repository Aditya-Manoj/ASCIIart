import tkinter as tk
import cv2
from PIL import Image

filepath = r'E:\IMPORTANT ONLY\Python Projects\img2txt\im3.jpg'
bstring = '@#W$9876543210?!abc;:+=-,._    '
stepsize = 10
print(bstring)
blen = len(bstring)
# print(blen)
den = 256/blen
# print(256/blen)
# print(255//den)
frame = cv2.imread(filepath, 0)
# print(frame[0][0])
# print(frame)
# print(frame.shape)
y = frame.shape[0]
x = frame.shape[1]
# print(y)
# print(x)
finaly = 100
finalx = int((100 * x) / y)
frame = cv2.resize(frame, (finalx, finaly))
print(frame.shape)
# print(frame.shape[0]*5, frame.shape[1]*5)
tkwinsize = str(frame.shape[1]*stepsize) + 'x' + str(frame.shape[0]*stepsize)
print(tkwinsize)
win = tk.Tk()
win.geometry(tkwinsize)
canvas = tk.Canvas(win, width=frame.shape[1]*stepsize, height=frame.shape[0]*stepsize)
# canvas.create_line(frame.shape[1]*stepsize, 0, frame.shape[1]*stepsize, frame.shape[0]*stepsize)
canvas.pack()

imstr = ""
for i in range(finaly):
    for j in range(finalx):
        fval = frame[i][j]
        bstrindex = int(fval//den)
        # print(bstring[bstrindex])
        # imstr += bstring[bstrindex]
        canvas.create_text(j*stepsize, i*stepsize, text=bstring[bstrindex])
    # imstr += '\n'

# win.mainloop()
canvas.update()
canvas.postscript(file="filen.eps")
# finalim = Image.open("filen.eps")
# finalim.save("filen.png", "png")

win.mainloop()

# print(imstr)
# with open('img.txt', 'w') as file:
#     file.write(imstr)
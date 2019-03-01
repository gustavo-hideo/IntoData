"""
GUSTAVO HIDEO HIGA CORREA
CS 450
06 PROVE: NEURAL NETWORKS PART 1
IMAGE
"""
#https://stackoverflow.com/questions/52146562/python-tkinter-paint-how-to-paint-smoothly-and-save-images-with-a-different"

    
from tkinter import *
#import tkinter as tk
import PIL
from PIL import Image, ImageDraw
import os
import io
import ghostscript
import PIL.ImageOps





def save():
    #filename = 'C:/DataScience/IntoData/BYUI/CS450 - Machine Learning and Data Mining/06 prove - Neural Networks/handwritten_number.png'
    #image1.save(filename)
   # cv.update()
    #cv.postscript(file = filename, colormode='gray')
    ps = cv.postscript(colormode='gray')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img = PIL.ImageOps.invert(img)
    img.save('C:/DataScience/IntoData/BYUI/CS450 - Machine Learning and Data Mining/06 prove - Neural Networks/handwritten_number.png')
    
def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y
    
def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), fill = 'red', width=20)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='black', width=20)
    lastx, lasty = x, y
    
def predict():
    exec(open('C:/DataScience/IntoData/BYUI/CS450 - Machine Learning and Data Mining/06 prove - Neural Networks/prediction.py').read())
    
def clear():
    cv.delete("all")
    #os.remove('C:/DataScience/IntoData/BYUI/CS450 - Machine Learning and Data Mining/06 prove - Neural Networks/handwritten_number.png')
    

    
    


root = Tk()

lastx, lasty = None, None

cv = Canvas(root, width = 640, height = 480, bg = 'black')

# --- PILplt.imshow(x_train[3105]
image1 = PIL.Image.new('RGB', (640, 480))
draw = ImageDraw.Draw(image1)

cv.bind('<1>', activate_paint)
cv.pack(expand = YES, fill = BOTH)

btn_save = Button(root, text = "save", command = save)
btn_save.pack()

btn_predict = Button(root, text = "predict", command = predict)
btn_predict.pack()

btn_clear = Button(root, text = "clear", command = clear)
btn_clear.pack()





root.mainloop()



#exec(open('C:/DataScience/IntoData/BYUI/CS450 - Machine Learning and Data Mining/06 prove - Neural Networks.py').read())


    

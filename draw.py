import tkinter as tk
import PIL
from PIL import Image, ImageDraw
import numpy as np
       
def save():
    global image_number
    filename = 'image_%d.jpg'%image_number   # image_number increments by 1 at every save
    image1.save(filename)
    image_number += 1
    cv.delete("all")
    draw.rectangle([(0,0),(im_w,im_l)], fill="white")



def paint(e):
    x, y = e.x, e.y
    x_pillow,y_pillow = x*im_w/400,y*im_l/300

    #canvas
    cv.create_oval(x-line_width_canvas,y+line_width_canvas,x+line_width_canvas,y-line_width_canvas,fill = "black")

    #pil
    draw.ellipse([(x_pillow-line_width,y_pillow-line_width),(x_pillow+line_width,y_pillow+line_width)], fill="black")
    cv.bind('<B1-Motion>', paint)

#config
line_width_canvas = 10
line_width = 1
im_w = 28
im_l = 28


root = tk.Tk()
image_number = 0
cv = tk.Canvas(root, width=400, height=300, bg='white')
# --- PIL
image1 = PIL.Image.new('RGB', (im_w, im_l), 'white')
draw = ImageDraw.Draw(image1)
cv.bind('<Button-1>', paint)
cv.pack(expand=tk.YES, fill=tk.BOTH)
btn_save = tk.Button(text="save", command=save)
btn_save.pack()
root.mainloop()
           
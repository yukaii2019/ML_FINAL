import tkinter as tk
import PIL
from PIL import Image, ImageDraw

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')



def save():
    image1.save('image.jpg')
    cv.delete("all")
    draw.rectangle([(0,0),(28,28)], fill="white")

def paint(e):
    x, y = e.x, e.y
    width = cv.winfo_width()
    height = cv.winfo_height()
    x_pillow,y_pillow = x*28/width,y*28/height

    #canvas
    cv.create_oval(x-10,y+10,x+10,y-10,fill = "black")

    #pil
    draw.ellipse([(x_pillow-1,y_pillow-1),(x_pillow+1,y_pillow+1)], fill="black")
    cv.bind('<B1-Motion>', paint)

def button_add():
    width = cv.winfo_width()
    height = cv.winfo_height()
   # print(width)
    #print(height)

    return

now_text = ''
def button_1():
    global now_text
    width = lbl_2.winfo_width()
    now_text = now_text + prediction_map[prediction[0]]
    #print((width-26)//25)
    if len(now_text)>(width-26)//25:   
        lbl_2["text"] = now_text[len(now_text)-(width-26)//25:]
    else:
        lbl_2["text"] = now_text

def button_2():
    global now_text
    width = lbl_2.winfo_width()
    now_text = now_text + prediction_map[prediction[1]]
    if len(now_text)>(width-26)//25:   
        lbl_2["text"] = now_text[len(now_text)-(width-26)//25:]
    else:
        lbl_2["text"] = now_text

def button_3():
    global now_text
    width = lbl_2.winfo_width()
    now_text = now_text + prediction_map[prediction[2]]
    if len(now_text)>(width-26)//25:   
        lbl_2["text"] = now_text[len(now_text)-(width-26)//25:]
    else:
        lbl_2["text"] = now_text

def button_4():
    global now_text
    width = lbl_2.winfo_width()
    now_text = now_text + prediction_map[prediction[3]]
    if len(now_text)>(width-26)//25:   
        lbl_2["text"] = now_text[len(now_text)-(width-26)//25:]
    else:
        lbl_2["text"] = now_text

def change_equation_bar(e):
    global now_text
    width = lbl_2.winfo_width()
    if len(now_text)>(width-26)//25:   
        lbl_2["text"] = now_text[len(now_text)-(width-26)//25:]
    else:
        lbl_2["text"] = now_text
prediction_map = {
    0:'0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'\N{PLUS SIGN}',
    11:'\N{HYPHEN-MINUS}',
    12:'\N{MULTIPLICATION SIGN}',
    13:'\N{DIVISION SIGN}',
    14:'\N{EQUALS SIGN}',
}


prediction = [0,1,2,14]

image1 = PIL.Image.new('RGB', (28, 28), 'white')
draw = ImageDraw.Draw(image1)




window = tk.Tk()
window.title("Calculator")

window.rowconfigure(0,weight = 1,minsize = 60)
window.rowconfigure(1,weight = 1,minsize = 85)
window.rowconfigure(2,weight = 1,minsize = 310)
window.columnconfigure(0,weight = 1,minsize = 110)
window.columnconfigure(1,weight = 1,minsize = 410)
window.columnconfigure(2,weight = 1,minsize = 110)

window.bind( "<Configure>", change_equation_bar)

frm_right_btn = tk.Frame(master = window, relief = tk.RIDGE, borderwidth = 5)
frm_right_btn.rowconfigure([0,1,2,3],weight = 1,minsize =75)
frm_right_btn.columnconfigure(0,weight = 1,minsize = 100)

frm_writing_board = tk.Frame(master = window, relief = tk.RIDGE, borderwidth = 5)
frm_writing_board.rowconfigure(0,weight = 1,minsize = 300)
frm_writing_board.columnconfigure(0,weight = 1,minsize = 400)

frm_display = tk.Frame(master = window, relief = tk.RIDGE, borderwidth = 5)
frm_display.rowconfigure(0,weight = 1,minsize = 75)
frm_display.columnconfigure(0,weight = 1,minsize = 600)

frm_left_btn = tk.Frame(master = window, relief = tk.RIDGE, borderwidth = 5)
frm_left_btn.rowconfigure([0,1,2,3],weight = 1,minsize =75)
frm_left_btn.columnconfigure([0,1],weight = 1,minsize = 50)

frm_display_equation = tk.Frame(master = window, relief = tk.RIDGE, borderwidth = 5)
frm_display_equation.rowconfigure(0,weight = 1,minsize = 50)
frm_display_equation.columnconfigure(0,weight = 1,minsize = 600)

frm_right_btn.grid(row = 2, column = 2, sticky="nsew")
frm_writing_board.grid(row = 2, column = 1, sticky="nsew")
frm_display.grid(row = 1, columnspan = 3, sticky="nsew")
frm_left_btn.grid(row = 2, column = 0, sticky="nsew")
frm_display_equation.grid(row = 0, columnspan = 3, sticky="nsew")


lbl_1 = tk.Label(master = frm_display, bg='white', relief = tk.RIDGE, borderwidth = 1)
lbl_1.grid(row = 0, column = 0, sticky="nsew")


lbl_2 = tk.Label(master = frm_display_equation, bg='white', relief = tk.RIDGE, borderwidth = 1,font = ("Courier",30),anchor = 'e',justify=tk.LEFT)
lbl_2.grid(row = 0, column = 0, sticky="nsew")


cv = tk.Canvas(master = frm_writing_board, bg='white', relief = tk.RIDGE, borderwidth = 1, width=400, height=300)
cv.grid(row = 0, column = 0,sticky="nsew")
cv.bind('<Button-1>', paint)

#right buttons
btn_1 = tk.Button(master = frm_right_btn, text = '1' ,relief = tk.RIDGE, borderwidth = 1, command = button_1)
btn_2 = tk.Button(master = frm_right_btn, text = '2' ,relief = tk.RIDGE, borderwidth = 1, command = button_2)
btn_3 = tk.Button(master = frm_right_btn, text = '3' ,relief = tk.RIDGE, borderwidth = 1, command = button_3)
btn_4 = tk.Button(master = frm_right_btn, text = '4' ,relief = tk.RIDGE, borderwidth = 1, command = button_4)
btn_1.grid(row = 0, column = 0,sticky="nsew")
btn_2.grid(row = 1, column = 0,sticky="nsew")
btn_3.grid(row = 2, column = 0,sticky="nsew")
btn_4.grid(row = 3, column = 0,sticky="nsew")


# left buttons
btn_5 = tk.Button(master = frm_left_btn, text = 'DEL', relief = tk.RIDGE, borderwidth = 1, command = button_add)
btn_6 = tk.Button(master = frm_left_btn, text = 'AC' , relief = tk.RIDGE, borderwidth = 1 , command = button_add)
btn_7 = tk.Button(master = frm_left_btn, text = "\N{RIGHTWARDS BLACK ARROW}", relief = tk.RIDGE, borderwidth = 1, command = button_add)
btn_8 = tk.Button(master = frm_left_btn, text = "\N{LEFTWARDS BLACK ARROW}" , relief = tk.RIDGE, borderwidth = 1, command = button_add)
btn_9 = tk.Button(master = frm_left_btn, text = '=', command = save, relief = tk.RIDGE, borderwidth = 1)


btn_5.grid(row = 0, columnspan = 2,sticky="nsew")
btn_6.grid(row = 1, columnspan = 2,sticky="nsew")
btn_7.grid(row = 2, column = 1,sticky="nsew")
btn_8.grid(row = 2, column = 0,sticky="nsew")
btn_9.grid(row = 3, columnspan = 2,sticky="nsew")




window.mainloop()
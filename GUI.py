import tkinter as tk
import PIL
from PIL import Image, ImageDraw


class GUI():
    def __init__(self):
        self.now_text = ''
        self.real_text = ''
        self.cursor = ' \N{BLACK DOWN-POINTING TRIANGLE} '
        self.prediction_map = {
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
        self.cursor_position = 0
        self.real_cursor_position = 0

    def save(self):
        self.image1.save('image.jpg')
        self.cv.delete("all")
        self.draw.rectangle([(0,0),(28,28)], fill="white")

    def paint(self,e):
        x, y = e.x, e.y
        width = self.cv.winfo_width()
        height = self.cv.winfo_height()
        x_pillow,y_pillow = x*28/width,y*28/height

        #canvas
        self.cv.create_oval(x-10,y+10,x+10,y-10,fill = "black")

        #pil
        self.draw.ellipse([(x_pillow-1,y_pillow-1),(x_pillow+1,y_pillow+1)], fill="black")
        self.cv.bind('<B1-Motion>', self.paint)

    def button_add(self):
        width = self.cv.winfo_width()
        height = self.cv.winfo_height()
        print(width)
        print(height)

        return

    def button_1(self):
        self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        self.real_text = self.real_text[:self.real_cursor_position]+self.prediction_map[self.prediction[0]]+self.real_text[self.real_cursor_position:]
        if self.cursor_position != self.equation_space:
            self.cursor_position = self.cursor_position + 1
            self.cursor = '   '+self.cursor
            self.lbl_3["text"] = self.cursor
        if self.real_cursor_position != len(self.real_text):
            self.real_cursor_position = self.real_cursor_position + 1
        self.lbl_2["text"] = self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1]

    def button_2(self):
        self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        self.real_text = self.real_text[:self.real_cursor_position]+self.prediction_map[self.prediction[1]]+self.real_text[self.real_cursor_position:]
        if self.cursor_position != self.equation_space:
            self.cursor_position = self.cursor_position + 1
            self.cursor = '   '+self.cursor
            self.lbl_3["text"] = self.cursor
        if self.real_cursor_position != len(self.real_text):
            self.real_cursor_position = self.real_cursor_position + 1
        self.lbl_2["text"] = self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1]

    def button_3(self):
        self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        self.real_text = self.real_text[:self.real_cursor_position]+self.prediction_map[self.prediction[2]]+self.real_text[self.real_cursor_position:]
        if self.cursor_position != self.equation_space:
            self.cursor_position = self.cursor_position + 1
            self.cursor = '   '+self.cursor
            self.lbl_3["text"] = self.cursor
        if self.real_cursor_position != len(self.real_text):
            self.real_cursor_position = self.real_cursor_position + 1
        self.lbl_2["text"] = self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1]

    def button_4(self):
        self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        self.real_text = self.real_text[:self.real_cursor_position]+self.prediction_map[self.prediction[3]]+self.real_text[self.real_cursor_position:]
        if self.cursor_position != self.equation_space:
            self.cursor_position = self.cursor_position + 1
            self.cursor = '   '+self.cursor
            self.lbl_3["text"] = self.cursor
        if self.real_cursor_position != len(self.real_text):
            self.real_cursor_position = self.real_cursor_position + 1
        self.lbl_2["text"] = self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1]
    def change_equation_bar(self,e):
        width = self.lbl_2.winfo_width()
        if len(self.now_text)>(width-26)//25:   
            self.lbl_2["text"] = self.now_text[len(self.now_text)-(width-26)//25:]
        else:
            self.lbl_2["text"] = self.now_text


    def left(self):
        self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        if self.cursor_position != 0:
            self.cursor_position = self.cursor_position - 1
            self.real_cursor_position = self.real_cursor_position - 1
            self.cursor = self.cursor[3:]
            self.lbl_3["text"] = self.cursor
        elif self.real_cursor_position  != 0:      
            self.real_cursor_position = self.real_cursor_position - 1
            self.lbl_2["text"] = self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1]
            


    def right(self):
        self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        if self.cursor_position != self.equation_space:
            self.cursor_position = self.cursor_position + 1
            self.real_cursor_position = self.real_cursor_position + 1
            self.cursor = '   '+self.cursor
            self.lbl_3["text"] = self.cursor
        elif self.real_cursor_position != len(self.real_text):
            self.real_cursor_position = self.real_cursor_position + 1
            self.lbl_2["text"] = self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1]
        

    def main(self, pred):
        self.prediction = pred
        
        self.window = tk.Tk()
        self.window.title("Calculator")

        self.image1 = PIL.Image.new('RGB', (28, 28), 'white')
        self.draw = ImageDraw.Draw(self.image1)

        self.window.rowconfigure(0,weight = 0,minsize = 25)
        self.window.rowconfigure(1,weight = 1,minsize = 60)
        self.window.rowconfigure(2,weight = 1,minsize = 85)
        self.window.rowconfigure(3,weight = 1,minsize = 310)
        self.window.columnconfigure(0,weight = 1,minsize = 110)
        self.window.columnconfigure(1,weight = 1,minsize = 410)
        self.window.columnconfigure(2,weight = 1,minsize = 110)

        self.window.bind( "<Configure>", self.change_equation_bar)

        self.frm_right_btn = tk.Frame(master = self.window, relief = tk.RIDGE, borderwidth = 5)
        self.frm_right_btn.rowconfigure([0,1,2,3],weight = 1,minsize =75)
        self.frm_right_btn.columnconfigure(0,weight = 1,minsize = 100)

        self.frm_writing_board = tk.Frame(master = self.window, relief = tk.RIDGE, borderwidth = 5)
        self.frm_writing_board.rowconfigure(0,weight = 1,minsize = 300)
        self.frm_writing_board.columnconfigure(0,weight = 1,minsize = 400)

        self.frm_display = tk.Frame(master = self.window, relief = tk.RIDGE, borderwidth = 5)
        self.frm_display.rowconfigure(0,weight = 1,minsize = 75)
        self.frm_display.columnconfigure(0,weight = 1,minsize = 600)

        self.frm_left_btn = tk.Frame(master =self.window, relief = tk.RIDGE, borderwidth = 5)
        self.frm_left_btn.rowconfigure([0,1,2,3],weight = 1,minsize =75)
        self.frm_left_btn.columnconfigure([0,1],weight = 1,minsize = 50)

        self.frm_display_equation = tk.Frame(master = self.window, relief = tk.RIDGE, borderwidth = 5)
        self.frm_display_equation.rowconfigure(0,weight = 1,minsize = 50)
        self.frm_display_equation.columnconfigure(0,weight = 1,minsize = 600)

        self.frm_cursor = tk.Frame(master = self.window, relief = tk.RIDGE, borderwidth = 5)
        self.frm_cursor.rowconfigure(0,weight = 1,minsize = 15)
        self.frm_cursor.columnconfigure(0,weight = 1,minsize = 600)

        self.frm_right_btn.grid(row = 3, column = 2, sticky="nsew")
        self.frm_writing_board.grid(row = 3, column = 1, sticky="nsew")
        self.frm_display.grid(row = 2, columnspan = 3, sticky="nsew")
        self.frm_left_btn.grid(row = 3, column = 0, sticky="nsew")
        self.frm_display_equation.grid(row = 1, columnspan = 3, sticky="nsew")
        self.frm_cursor.grid(row = 0, columnspan = 3, sticky="nsew")


        self.lbl_1 = tk.Label(master = self.frm_display, bg='white', relief = tk.RIDGE, borderwidth = 1)
        self.lbl_1.grid(row = 0, column = 0, sticky="nsew")


        self.lbl_2 = tk.Label(master = self.frm_display_equation, bg='white', relief = tk.RIDGE, borderwidth = 1,font = ("Courier",30),anchor = 'w',justify=tk.RIGHT)
        self.lbl_2.grid(row = 0, column = 0, sticky="nsew")

        self.lbl_3 = tk.Label(master = self.frm_cursor, bg='white', relief = tk.RIDGE, borderwidth = 1,font = ("Courier",10),anchor = 'w',justify=tk.RIGHT,text = self.cursor )
        self.lbl_3.grid(row = 0, column = 0, sticky="nsew")

        self.cv = tk.Canvas(master = self.frm_writing_board, bg='white', relief = tk.RIDGE, borderwidth = 1, width=400, height=300)
        self.cv.grid(row = 0, column = 0,sticky="nsew")
        self.cv.bind('<Button-1>', self.paint)

        #right buttons
        self.btn_1 = tk.Button(master = self.frm_right_btn, text = '1' ,relief = tk.RIDGE, borderwidth = 1, command = self.button_1)
        self.btn_2 = tk.Button(master = self.frm_right_btn, text = '2' ,relief = tk.RIDGE, borderwidth = 1, command = self.button_2)
        self.btn_3 = tk.Button(master = self.frm_right_btn, text = '3' ,relief = tk.RIDGE, borderwidth = 1, command = self.button_3)
        self.btn_4 = tk.Button(master = self.frm_right_btn, text = '4' ,relief = tk.RIDGE, borderwidth = 1, command = self.button_4)
        self.btn_1.grid(row = 0, column = 0,sticky="nsew")
        self.btn_2.grid(row = 1, column = 0,sticky="nsew")
        self.btn_3.grid(row = 2, column = 0,sticky="nsew")
        self.btn_4.grid(row = 3, column = 0,sticky="nsew")


        # left buttons
        self.btn_5 = tk.Button(master = self.frm_left_btn, text = 'DEL', relief = tk.RIDGE, borderwidth = 1, command = self.button_add)
        self.btn_6 = tk.Button(master = self.frm_left_btn, text = 'AC' , relief = tk.RIDGE, borderwidth = 1 , command = self.button_add)
        self.btn_7 = tk.Button(master = self.frm_left_btn, text = "\N{RIGHTWARDS BLACK ARROW}", relief = tk.RIDGE, borderwidth = 1, command = self.right)
        self.btn_8 = tk.Button(master = self.frm_left_btn, text = "\N{LEFTWARDS BLACK ARROW}" , relief = tk.RIDGE, borderwidth = 1, command = self.left)
        self.btn_9 = tk.Button(master = self.frm_left_btn, text = '=', command = self.save, relief = tk.RIDGE, borderwidth = 1)


        self.btn_5.grid(row = 0, columnspan = 2,sticky="nsew")
        self.btn_6.grid(row = 1, columnspan = 2,sticky="nsew")
        self.btn_7.grid(row = 2, column = 1,sticky="nsew")
        self.btn_8.grid(row = 2, column = 0,sticky="nsew")
        self.btn_9.grid(row = 3, columnspan = 2,sticky="nsew")

        
        
        
        self.window.mainloop()

gui = GUI()
prediction = [0,1,2,14] 
gui.main(prediction)




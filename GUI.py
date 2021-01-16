import tkinter as tk
import numpy as np
from inference import inference
import PIL
from PIL import Image, ImageDraw
from calculator import * 
import re

class GUI():
    def __init__(self):
        self.now_text = ''
        self.real_text = ''
        self.visual_text = ''
        self.cursor_text = ''
        self.cursor = ' \N{BLACK DOWN-POINTING TRIANGLE} '
        self.prediction_map = {
                            0:  '0',
                            1:  '1',
                            2:  '2',
                            3:  '3',
                            4:  '4',
                            5:  '5',
                            6:  '6',
                            7:  '7',
                            8:  '8',
                            9:  '9',
                            10: 'a',
                            11: 'b',
                            12: 'c',
                            13: 'd',
                            14: 'e',
                            15: 'f',
                            16: 'g',
                            17: 'h',
                            18: 'i',
                            19: 'j',
                            20: 'k',
                            21: 'l',
                            22: 'm',
                            23: 'n',
                            24: 'o',
                            25: 'p',
                            26: 'q',
                            27: 'r',
                            28: 's'
                        }
        self.visual_map = {
                            '0':'0',
                            '1':'1',
                            '2':'2',
                            '3':'3',
                            '4':'4',
                            '5':'5',
                            '6':'6',
                            '7':'7',
                            '8':'8',
                            '9':'9',
                            'a':'\N{PLUS SIGN}',
                            'b':'\N{HYPHEN-MINUS}',
                            'c':'\N{MULTIPLICATION SIGN}',
                            'd':'\N{DIVISION SIGN}',
                            'e':'\N{EQUALS SIGN}',
                            'f':'\N{Greek Small Letter Pi}',
                            'g':'e',
                            'h':'ln',  #ln
                            'i':'log', #log
                            'j':'cos',
                            'k':'sin',
                            'l':'tan',
                            'm':'\N{Circumflex Accent}',  # ^
                            'n':'\N{Square Root}',
                            'o':'(',
                            'p':')',
                            'q':'%',
                            'r':'!',
                            's':'.'
                        }
        self.cursor_position = 0
        self.real_cursor_position = 0
        self.visual_cursor_position = 0
        self.ans = '12349876' 

        self.image1 = PIL.Image.new('RGB', (28, 28), 'white')
        self.draw = ImageDraw.Draw(self.image1) 

        self.inf = inference()
        self.prediction = [18,17,16,19]
        self.probability = [0, 0 , 0, 0]
        self.equation_space = 24
        self.now_eq_length = 0

    def visualize_real_text(self,string):
        return ''.join(list(map(lambda x: self.visual_map[x],string)))
    def clean_board_and_button(self):
        self.cv.delete("all")
        self.draw.rectangle([(0,0),(28,28)], fill="white")
        self.btn_1['text'] = ''
        self.btn_2['text'] = ''
        self.btn_3['text'] = ''
        self.btn_4['text'] = ''

    def paint(self,e):
        x, y = e.x, e.y
        width = self.cv.winfo_width()
        height = self.cv.winfo_height()
        x_pillow,y_pillow = x*28/width,y*28/height
        
        #canvas
        self.cv.create_oval(x-12,y+12,x+12,y-12,fill = "black")
        #self.cv.create_rectangle(x-12,y+12,x+12,y-12,fill = "black")
        #pil
        self.draw.ellipse([(x_pillow-1,y_pillow-1),(x_pillow+1,y_pillow+1)], fill="black")

        #inference 
        img_grey = self.image1.convert('L')
        array = np.array(img_grey).reshape(-1,28,28,1)
        self.prediction, self.probability = self.inf.label_prob(array)
        self.change_right_buttons()
        self.cv.bind('<B1-Motion>', self.paint)

    def button_add(self):
        width = self.cv.winfo_width()
        height = self.cv.winfo_height()
        print(width)
        print(height)

        return

    def button_1(self):
        #self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        enter = self.prediction_map[self.prediction[0]]

        self.now_eq_length = self.now_eq_length + 2 if enter == 'h' else (self.now_eq_length + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.now_eq_length + 1) 
        self.cursor_position = self.cursor_position + 2 if enter == 'h' else (self.cursor_position + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.cursor_position + 1)
        self.visual_cursor_position = self.visual_cursor_position + 2 if enter == 'h' else (self.visual_cursor_position + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.visual_cursor_position + 1)
        self.real_cursor_position = self.real_cursor_position + 1

        if self.cursor_position >= self.equation_space:
            self.cursor_position = self.equation_space - 1
        

        self.real_text = self.real_text[:self.real_cursor_position-1] + enter + self.real_text[self.real_cursor_position-1:]

        self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.visual_cursor_position + (self.equation_space-self.cursor_position) + 1]

        self.cursor_text = '   '*(self.cursor_position) +self.cursor

        self.lbl_3["text"] = self.cursor_text
        self.lbl_2["text"] = self.visual_text

        self.clean_board_and_button()
        #self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1]


        #self.real_text = self.real_text[:self.real_cursor_position]+ enter + self.real_text[self.real_cursor_position:]  #insert 
        #self.visual_text = self.visualize_real_text(self.real_text)[-self.equation_space:]
        '''
        if self.cursor_position != self.equation_space:
            self.cursor_position = self.cursor_position + 1
            self.cursor = '   '+self.cursor
            self.lbl_3["text"] = self.cursor
        if self.real_cursor_position != len(self.real_text):
            self.real_cursor_position = self.real_cursor_position + 1
        self.lbl_2["text"] = self.visualize_real_text(self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1])
        self.clean_board_and_button()
        '''
    def button_2(self):
        enter = self.prediction_map[self.prediction[1]]

        self.now_eq_length = self.now_eq_length + 2 if enter == 'h' else (self.now_eq_length + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.now_eq_length + 1) 
        self.cursor_position = self.cursor_position + 2 if enter == 'h' else (self.cursor_position + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.cursor_position + 1)
        self.visual_cursor_position = self.visual_cursor_position + 2 if enter == 'h' else (self.visual_cursor_position + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.visual_cursor_position + 1)
        self.real_cursor_position = self.real_cursor_position + 1

        if self.cursor_position >= self.equation_space:
            self.cursor_position = self.equation_space - 1
        

        self.real_text = self.real_text[:self.real_cursor_position-1] + enter + self.real_text[self.real_cursor_position-1:]

        self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.visual_cursor_position + (self.equation_space-self.cursor_position) + 1]

        self.cursor_text = '   '*(self.cursor_position) +self.cursor

        self.lbl_3["text"] = self.cursor_text
        self.lbl_2["text"] = self.visual_text

        self.clean_board_and_button()
        '''
        #self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        self.real_text = self.real_text[:self.real_cursor_position]+self.prediction_map[self.prediction[1]]+self.real_text[self.real_cursor_position:]
        if self.cursor_position != self.equation_space:
            self.cursor_position = self.cursor_position + 1
            self.cursor = '   '+self.cursor
            self.lbl_3["text"] = self.cursor
        if self.real_cursor_position != len(self.real_text):
            self.real_cursor_position = self.real_cursor_position + 1
        self.lbl_2["text"] = self.visualize_real_text(self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1])
        self.clean_board_and_button()
        '''
    def button_3(self):
        enter = self.prediction_map[self.prediction[2]]

        self.now_eq_length = self.now_eq_length + 2 if enter == 'h' else (self.now_eq_length + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.now_eq_length + 1) 
        self.cursor_position = self.cursor_position + 2 if enter == 'h' else (self.cursor_position + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.cursor_position + 1)
        self.visual_cursor_position = self.visual_cursor_position + 2 if enter == 'h' else (self.visual_cursor_position + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.visual_cursor_position + 1)
        self.real_cursor_position = self.real_cursor_position + 1

        if self.cursor_position >= self.equation_space:
            self.cursor_position = self.equation_space - 1
        

        self.real_text = self.real_text[:self.real_cursor_position-1] + enter + self.real_text[self.real_cursor_position-1:]

        self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.visual_cursor_position + (self.equation_space-self.cursor_position) + 1]

        self.cursor_text = '   '*(self.cursor_position) +self.cursor

        self.lbl_3["text"] = self.cursor_text
        self.lbl_2["text"] = self.visual_text

        self.clean_board_and_button()
        '''
        #self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        self.real_text = self.real_text[:self.real_cursor_position]+self.prediction_map[self.prediction[2]]+self.real_text[self.real_cursor_position:]
        if self.cursor_position != self.equation_space:
            self.cursor_position = self.cursor_position + 1
            self.cursor = '   '+self.cursor
            self.lbl_3["text"] = self.cursor
        if self.real_cursor_position != len(self.real_text):
            self.real_cursor_position = self.real_cursor_position + 1
        self.lbl_2["text"] = self.visualize_real_text(self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1])
        self.clean_board_and_button()
        '''
    def button_4(self):
        enter = self.prediction_map[self.prediction[3]]
        '''  '''
        self.now_eq_length = self.now_eq_length + 2 if enter == 'h' else (self.now_eq_length + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.now_eq_length + 1) 
        '''   '''
        self.cursor_position = self.cursor_position + 2 if enter == 'h' else (self.cursor_position + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.cursor_position + 1)
        self.visual_cursor_position = self.visual_cursor_position + 2 if enter == 'h' else (self.visual_cursor_position + 3 if enter == 'i' or enter == 'j' or enter == 'k' or enter == 'l' else self.visual_cursor_position + 1)
        self.real_cursor_position = self.real_cursor_position + 1

        if self.cursor_position >= self.equation_space:
            self.cursor_position = self.equation_space - 1
        

        self.real_text = self.real_text[:self.real_cursor_position-1] + enter + self.real_text[self.real_cursor_position-1:]

        self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.visual_cursor_position + (self.equation_space-self.cursor_position) + 1]

        self.cursor_text = '   '*(self.cursor_position) +self.cursor

        self.lbl_3["text"] = self.cursor_text
        self.lbl_2["text"] = self.visual_text

        self.clean_board_and_button()
        '''
        #self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        self.real_text = self.real_text[:self.real_cursor_position]+self.prediction_map[self.prediction[3]]+self.real_text[self.real_cursor_position:]
        if self.cursor_position != self.equation_space:
            self.cursor_position = self.cursor_position + 1
            self.cursor = '   '+self.cursor
            self.lbl_3["text"] = self.cursor
        if self.real_cursor_position != len(self.real_text):
            self.real_cursor_position = self.real_cursor_position + 1
        self.lbl_2["text"] = self.visualize_real_text(self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1])
        self.clean_board_and_button()
        '''
    def change_equation_bar(self,e):
        self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        self.lbl_2["text"] = self.visualize_real_text(self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1])
    
    def left(self):
        if self.real_cursor_position > 0:
            #self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
            the_word_before = self.real_text[self.real_cursor_position-1]
            cursor_shift = 2 if the_word_before == 'h' else (3 if the_word_before == 'i' or the_word_before == 'j' or the_word_before == 'k' or the_word_before == 'l' else 1)
            self.cursor_position = self.cursor_position-cursor_shift
            self.visual_cursor_position = self.visual_cursor_position-cursor_shift
            self.real_cursor_position = self.real_cursor_position - 1 
            if self.cursor_position < 0:
                self.cursor_position = 0
            if self.visual_cursor_position < 0:
                self.visual_cursor_position = 0
            if self.real_cursor_position < 0:
                self.real_cursor_position = 0 

            self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.visual_cursor_position + (self.equation_space-self.cursor_position) + 1]
            '''
            if self.now_eq_length - self.visual_cursor_position <=  self.equation_space-self.cursor_position:
                self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position: self.now_eq_length]
            else:
                self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.visual_cursor_position + (self.equation_space-self.cursor_position) + 1]
            '''
            
            #self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.now_eq_length]
            self.cursor_text = '   '*(self.cursor_position) +self.cursor

            self.lbl_3["text"] = self.cursor_text
            self.lbl_2["text"] = self.visual_text

        '''
        if self.cursor_position != 0:
            self.cursor_position = self.cursor_position - 1
            self.real_cursor_position = self.real_cursor_position - 1
            self.cursor = self.cursor[3:]
            self.lbl_3["text"] = self.cursor
        elif self.real_cursor_position  != 0:      
            self.real_cursor_position = self.real_cursor_position - 1
            self.lbl_2["text"] = self.visualize_real_text(self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1])
        '''
    def right(self):
        if self.real_cursor_position < len(self.real_text):
            the_word_after = self.real_text[self.real_cursor_position]
            cursor_shift = 2 if the_word_after == 'h' else (3 if the_word_after == 'i' or the_word_after == 'j' or the_word_after == 'k' or the_word_after == 'l' else 1)
            self.cursor_position = self.cursor_position+cursor_shift
            self.visual_cursor_position = self.visual_cursor_position+cursor_shift
            self.real_cursor_position = self.real_cursor_position + 1 
            if self.cursor_position >= self.equation_space:
                self.cursor_position = self.equation_space - 1
            '''
            if self.real_cursor_position > len(self.real_text):
                self.real_cursor_position = len(self.real_text)
            '''

        self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.visual_cursor_position + (self.equation_space-self.cursor_position) + 1]
        '''
            if self.now_eq_length - self.visual_cursor_position <=  self.equation_space-self.cursor_position:
                self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position: self.now_eq_length]
            else:
                self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.visual_cursor_position + (self.equation_space-self.cursor_position) + 1]
        '''
        #self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.now_eq_length]
        self.cursor_text = '   '*(self.cursor_position) +self.cursor

        self.lbl_3["text"] = self.cursor_text
        self.lbl_2["text"] = self.visual_text
        '''
        self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        if self.cursor_position != self.equation_space and self.real_cursor_position != len(self.real_text):
            self.cursor_position = self.cursor_position + 1
            self.real_cursor_position = self.real_cursor_position + 1
            self.cursor = '   '+self.cursor
            self.lbl_3["text"] = self.cursor
        elif self.real_cursor_position != len(self.real_text):
            self.real_cursor_position = self.real_cursor_position + 1
            self.lbl_2["text"] = self.visualize_real_text(self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1])
        '''
    def DEL(self): 
        if self.real_cursor_position > 0:
            #self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
            the_word_before = self.real_text[self.real_cursor_position-1]
            cursor_shift = 2 if the_word_before == 'h' else (3 if the_word_before == 'i' or the_word_before == 'j' or the_word_before == 'k' or the_word_before == 'l' else 1)
            self.cursor_position = self.cursor_position-cursor_shift
            self.visual_cursor_position = self.visual_cursor_position-cursor_shift
            self.real_cursor_position = self.real_cursor_position - 1 
            if self.cursor_position < 0:
                self.cursor_position = 0
            if self.visual_cursor_position < 0:
                self.visual_cursor_position = 0
            if self.real_cursor_position < 0:
                self.real_cursor_position = 0 

            self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position:self.visual_cursor_position] + self.visualize_real_text(self.real_text)[self.visual_cursor_position+cursor_shift:self.visual_cursor_position + (self.equation_space-self.cursor_position) + 1]
            self.real_text = self.real_text[:self.real_cursor_position] + self.real_text[self.real_cursor_position+1:] 
            '''
            if self.now_eq_length - self.visual_cursor_position <=  self.equation_space-self.cursor_position :
                self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.now_eq_length-cursor_shift_b]
            else:
                self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.visual_cursor_position + (self.equation_space-self.cursor_position)+1-cursor_shift_b]
             '''
            #self.visual_text = self.visualize_real_text(self.real_text)[self.visual_cursor_position - self.cursor_position : self.visual_cursor_position + (self.equation_space-self.cursor_position-cursor_shift_b )+1]


            self.cursor_text = '   '*(self.cursor_position) +self.cursor
            self.lbl_3["text"] = self.cursor_text
            self.lbl_2["text"] = self.visual_text
        
        '''
        if self.cursor_position != 0:
            if self.cursor_position == self.real_cursor_position:
                self.cursor = self.cursor[3:]
                self.cursor_position = self.cursor_position - 1
                self.real_cursor_position = self.real_cursor_position - 1
                self.lbl_3["text"] = self.cursor
                self.real_text = self.real_text[0:self.real_cursor_position] + self.real_text[self.real_cursor_position+1:]
                self.lbl_2["text"] = self.visualize_real_text(self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)])
            else:
                self.real_cursor_position = self.real_cursor_position - 1
                self.lbl_3["text"] = self.cursor
                self.real_text = self.real_text[0:self.real_cursor_position] + self.real_text[self.real_cursor_position+1:]
                self.lbl_2["text"] = self.visualize_real_text(self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)])
        '''
            
    def AC(self):
        #self.equation_space =  (self.frm_display_equation.winfo_width()-26)//25
        self.real_cursor_position = 0
        self.cursor_position = 0
        self.visual_cursor_position = 0
        self.real_text = ''
        self.lbl_1['text'] =''
        self.now_eq_length = 0
        self.lbl_3["text"] = self.cursor
        self.lbl_2["text"] = self.visualize_real_text(self.real_text[self.real_cursor_position-self.cursor_position:self.real_cursor_position+(self.equation_space-self.cursor_position)+1])
        self.clean_board_and_button()

    def change_right_buttons(self):
        if self.probability[0] > 52:
            self.btn_1['text'] = str(self.visual_map[self.prediction_map[self.prediction[0]]]) + '\n' + str(self.probability[0]) + 'pt'
        else:
            self.btn_1['text'] = ''
        if self.probability[1] > 52:
            self.btn_2['text'] = str(self.visual_map[self.prediction_map[self.prediction[1]]]) + '\n' + str(self.probability[1]) + 'pt'
        else:
            self.btn_2['text'] = ''
        if self.probability[2] > 52:
            self.btn_3['text'] = str(self.visual_map[self.prediction_map[self.prediction[2]]]) + '\n' + str(self.probability[2]) + 'pt'
        else:
            self.btn_3['text'] = ''
        if self.probability[3] > 52:
            self.btn_4['text'] = str(self.visual_map[self.prediction_map[self.prediction[3]]]) + '\n' + str(self.probability[3]) + 'pt'
        else:
            self.btn_4['text'] = ''
    def transformer(self,lst):
        lst = "".join(['.' if lst[x]=='s'else \
                    ('-'if lst[x]=='b' and x!=len(lst) and lst[x+1].isdigit() else \
                        lst[x]) for x in range(len(lst))])
                        #lst = '1a3co-9.8pbjo40p'  #1+3*(-9.8)-cos(40)
        numbers = [float(x) for x in re.findall('[+-]?\d+(?:\.\d+)?',lst)]
        equation = re.sub('[+-]?\d+(?:\.\d+)?','A',lst)
        inv_map = {v: k for k, v in self.prediction_map.items()}
        equation_list = [ x if x == 'A' else str(inv_map[x]) for x in equation]
        insert_multiplier_pos = []
        k = 1
        for i in range(len(equation_list)-1):
            if equation_list[i] == 'A' and (equation_list[i+1] == '15' or equation_list[i+1] == '16' or equation_list[i+1] == '17' or equation_list[i+1] == '18' or \
                                            equation_list[i+1] == '19' or equation_list[i+1] == '20' or equation_list[i+1] == '21' or equation_list[i+1] == '23' or\
                                            equation_list[i+1] == '24'):
                insert_multiplier_pos.append(i+k)
                k+=1
        for i in insert_multiplier_pos:
            equation_list.insert(i,'12')
        print(equation_list)
        return equation_list, numbers
        
    def show_answer(self):
        equation_list, numbers = self.transformer(self.real_text)
        print(equation_list)
        print(numbers)
        ans = cal(equation_list,numbers)
        self.lbl_1['text'] = ans
    def main(self):  
        
        self.window = tk.Tk()
        self.window.title("Calculator")

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


        self.lbl_1 = tk.Label(master = self.frm_display, bg='#A9BAB6', relief = tk.RIDGE, borderwidth = 1,font = ("Courier",30),anchor = 'e',justify=tk.LEFT)
        self.lbl_1.grid(row = 0, column = 0, sticky="nsew")


        self.lbl_2 = tk.Label(master = self.frm_display_equation, bg='#A9BAB6', relief = tk.RIDGE, borderwidth = 1,font = ("Courier",30),anchor = 'w',justify=tk.RIGHT)
        self.lbl_2.grid(row = 0, column = 0, sticky="nsew")

        self.lbl_3 = tk.Label(master = self.frm_cursor, bg='#114E6A', relief = tk.RIDGE, borderwidth = 1,font = ("Courier",10),anchor = 'w',justify=tk.RIGHT,text = self.cursor,fg = '#F8F5F5')
        self.lbl_3.grid(row = 0, column = 0, sticky="nsew")

        self.cv = tk.Canvas(master = self.frm_writing_board, bg='white', relief = tk.RIDGE, borderwidth = 1, width=400, height=300)
        self.cv.grid(row = 0, column = 0,sticky="nsew")
        self.cv.bind('<Button-1>', self.paint)

        #right buttons
        self.btn_1 = tk.Button(master = self.frm_right_btn ,relief = tk.RIDGE, borderwidth = 1, font = ("Courier",15,'bold'),command = self.button_1,bg = '#2E2B2A' ,fg = '#F8F5F5')
        self.btn_2 = tk.Button(master = self.frm_right_btn ,relief = tk.RIDGE, borderwidth = 1, font = ("Courier",15,'bold'),command = self.button_2,bg = '#2E2B2A' ,fg = '#F8F5F5')
        self.btn_3 = tk.Button(master = self.frm_right_btn ,relief = tk.RIDGE, borderwidth = 1, font = ("Courier",15,'bold'),command = self.button_3,bg = '#2E2B2A' ,fg = '#F8F5F5')
        self.btn_4 = tk.Button(master = self.frm_right_btn ,relief = tk.RIDGE, borderwidth = 1, font = ("Courier",15,'bold'),command = self.button_4,bg = '#2E2B2A' ,fg = '#F8F5F5')
        self.btn_1.grid(row = 0, column = 0,sticky="nsew")
        self.btn_2.grid(row = 1, column = 0,sticky="nsew")
        self.btn_3.grid(row = 2, column = 0,sticky="nsew")
        self.btn_4.grid(row = 3, column = 0,sticky="nsew")


        # left buttons
        self.btn_5 = tk.Button(master = self.frm_left_btn, text = 'DEL'                       , relief = tk.RIDGE,font = ("Courier",15,'bold'),borderwidth = 1, command = self.DEL)
        self.btn_6 = tk.Button(master = self.frm_left_btn, text = 'AC'                        , relief = tk.RIDGE,font = ("Courier",15,'bold'),borderwidth = 1, command = self.AC)
        self.btn_7 = tk.Button(master = self.frm_left_btn, text = "\N{RIGHTWARDS BLACK ARROW}", relief = tk.RIDGE,font = ("Courier",15,'bold'),borderwidth = 1, command = self.right)
        self.btn_8 = tk.Button(master = self.frm_left_btn, text = "\N{LEFTWARDS BLACK ARROW}" , relief = tk.RIDGE,font = ("Courier",15,'bold'),borderwidth = 1, command = self.left)
        self.btn_9 = tk.Button(master = self.frm_left_btn, text = 'CAL',bg = '#114E6A',fg = '#F8F5F5', relief = tk.RIDGE,font = ("Courier",15,'bold'),borderwidth = 1, command = self.show_answer)


        self.btn_5.grid(row = 0, columnspan = 2,sticky="nsew")
        self.btn_6.grid(row = 1, columnspan = 2,sticky="nsew")
        self.btn_7.grid(row = 2, column = 1,sticky="nsew")
        self.btn_8.grid(row = 2, column = 0,sticky="nsew")
        self.btn_9.grid(row = 3, columnspan = 2,sticky="nsew")

        
        
        
        self.window.mainloop()

gui = GUI()
gui.main()




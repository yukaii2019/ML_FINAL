import numpy as np
import re
encode_map = {
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
prediction_map = {
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
def transformer(lst):
    lst = "".join(['.' if lst[x]=='s'else \
                ('-'if lst[x]=='b' and x!=len(lst) and lst[x+1].isdigit() else \
                    lst[x]) for x in range(len(lst))])
                    #lst = '1a3co-9.8pbjo40p'  #1+3*(-9.8)-cos(40)
    numbers = re.findall('[+-]?\d+(?:\.\d+)?',lst)
    equation = re.sub('[+-]?\d+(?:\.\d+)?','A',lst)
    inv_map = {v: k for k, v in encode_map.items()}
    equation_list = [x if x == 'A' else inv_map[x] for x in equation]
    '''
    equation_lst = []
    k = 65
    for i in equation:
        if i =='D':
            equation_lst.append(chr(k))
            k = k+1
        else:
            equation_lst.append(inv_map[i])
    '''
    print(numbers)
    print(equation_list)

equation_test = '1a3cob9s8pajo40p'  #1+3*(-9.8)+cos(40)
transformer(equation_test)
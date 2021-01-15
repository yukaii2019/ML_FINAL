import numpy as np
class Stacks:
    def __init__(self):
        self.items = []

    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []
    
    def printStack(self):
        return self.items
    def sizes(self):
        return len(self.items)

# converts infix expression to postfix expression
def infix_to_postfix(st,priority,inf):
    pst = []
    for el in inf:
        if el == ' ':
            continue
        if el == '24':
            st.push(el)

        elif el == '25':
            while not st.is_empty():
                if st.peek() == '24':
                    st.pop()
                    break
                else:
                    pst.append(st.pop())
        elif el not in priority.keys() and (el != '24' or el != '25'):
           
            pst.append(el)

        elif el in priority.keys() and  st.is_empty():

            st.push(el)

        elif el in priority.keys() and not st.is_empty() and st.peek() =='24':
            # print("operator:",el)
            st.push(el)
        elif el in priority.keys() and not st.is_empty() and priority[el] >= priority[st.peek()]:
            # print("operator: ",el)
            st.push(el)

        elif el in priority.keys() and not st.is_empty() and priority[el] < priority[st.peek()]:
            #print("operator: ",el)
            while not st.is_empty():
                if st.peek() == '25':
                    break
                elif st.peek()!='24' and priority[st.peek()] >= priority[el]:
                    pst.append(st.pop())
                else:
                    break
            st.push(el)

    while not st.is_empty():
        pst.append(st.pop())
    return pst

def reverse(exp):
    rev_exp = []
    for i in range(len(exp)-1,-1,-1):
        if exp[i] == '(':
            e = ')'
        elif exp[i] == ')':
            e = '('
        else:
            e = exp[i]
        rev_exp.append(e)
    return rev_exp

def infix_to_prefix(st,priority,inf):
    rev_exp = reverse(inf)
    pst = infix_to_postfix(st,priority,rev_exp)
    return reverse(pst)
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
    
def isoperator(a):
    if a=='10' or a=='11'or a=='12'or a=='13'or a=='17'or a=='18'or a=='19'or a=='20'or a=='21'or a=='22'\
                    or a=='26'or a=='27'or a=='23':
        return 1
    else:
        return 0
def calculator(s,reference):
    C=Stacks()
    j=0
    for ss in s:
        print("now:",ss)
        print(C.printStack())
        if isoperator(ss):
            print(C.sizes())
            if(C.sizes()>=2):
                if ss=='10':
                    a=float(C.pop())
                    b=float(C.pop())
                    C.push(add(a,b))
                elif ss=='11':
                    a=float(C.pop())
                    b=float(C.pop())
                    C.push(subtract(b,a))
                elif ss=='12':
                    a=float(C.pop())
                    b=float(C.pop())
                    C.push(multiply(a,b))
                elif ss=='13':
                    a=float(C.pop())
                    b=float(C.pop())
                    C.push(divide(b,a))
                elif ss=='22':
                    a=float(C.pop()) 
                    b=float(C.pop())
                    C.push(np.power(b,a))
                elif ss=='26':
                    a=float(C.pop()) 
                    b=float(C.pop())
                    C.push(b%a)     
                elif ss=='17': #ln
                    a=float(C.pop())
                    C.push(np.log(a))
                elif ss=='18':
                    a=float(C.pop()) #log
                    C.push(np.log10(a))
                elif ss=='19': #cos
                    a=float(C.pop()) 
                    C.push(np.cos(a))
                elif ss=='20': #sin
                    a=float(C.pop()) 
                    C.push(np.sin(a))
                elif ss=='21': #tan
                    a=float(C.pop()) 
                    C.push(np.tan(a))
                elif ss=='23': #sqrt
                    a=float(C.pop())
                    C.push(np.sqrt(a))
                elif ss=='27': #!
                    a=float(C.pop())
                    C.push(np.math.factorial(a))  
            else:
                if ss=='17': #ln
                    a=float(C.pop())
                    C.push(np.log(a))
                elif ss=='18':
                    a=float(C.pop()) #log
                    C.push(np.log10(a))
                elif ss=='19': #cos
                    a=float(C.pop()) 
                    C.push(np.cos(a))
                elif ss=='20': #sin
                    a=float(C.pop()) 
                    C.push(np.sin(a))
                elif ss=='21': #tan
                    a=float(C.pop()) 
                    C.push(np.tan(a))
                elif ss=='23': #sqrt
                    a=float(C.pop())
                    C.push(np.sqrt(a))
                elif ss=='27': #!
                    a=float(C.pop())
                    C.push(np.math.factorial(a))                    

                    
                
        elif(ss=="A"):
            C.push(float(reference[j]))
            j+=1
        elif(ss=="15"):
            C.push(np.pi)
        elif(ss=="16"):
            C.push(np.exp(1))
            
    return float(C.pop())     

def cal(inf,reference_list):
    priority = {}
    priority['10'] = 1
    priority['11'] = 1
    priority['12'] = 2
    priority['13'] = 2

    priority['17'] = 3
    priority['18'] = 3
    priority['19'] = 3
    priority['20'] = 3
    priority['21'] = 3
    priority['23'] = 3

    priority['22'] = 4 #^
    priority['26'] = 4 #%
    priority['27'] = 4 #!
    st = Stacks()
    #inf = input("Enter the infix expression:")
    #print("input: a+b*(c^d-e)^(f+g*h)-i")
    #inf = "a+b*(c^d-e)^(f+g*h)-i"

    #inf=['2','12','2','10','3']
    #inf=['24','A','10','A','25','12','24','A','11','A','25']
    #reference_list=[10, 3, 101, 1]

    #inf=['A','13','A','12','A','10','A']
    #reference_list=[9,3,5,88]
    #inf=['23','20','A']
    #reference_list=[38]

    postfix=infix_to_postfix(st,priority,inf)
    print(postfix)


    return calculator(postfix,reference_list)



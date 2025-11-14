import tkinter as tk
from tkinter import *

class Stack:
    def __init__(self):
        self.elements=[]

    def push(self,input_box):
        self.elements.append(input_box.get(1.0,"end-1c"))

    def pop(self):
        if len(self.elements) !=0:
            self.elements.pop()

    def display(self,dis_box):
        if len(self.elements) != 0:
            str_ele=self.elements[0]

            for ele in self.elements[1:]:
                str_ele=str_ele+f",{ele}"

            dis_box.delete(1.0,tk.END)
            dis_box.insert(tk.INSERT,str_ele)

m_stacks=[Stack()]
m_sele_stack=m_stacks[0]

def create_stack():
    m_stacks.append(Stack())

def select_stack(x):
    global m_sele_stack
    m_sele_stack=m_stacks[x]

top=tk.Tk()

top.geometry("300x375")
view_box=tk.Text(top,width=150,height=1)
view_box.place(x=0,y=50)
input_box=tk.Text(top,width=150,height=1)
input_box.place(x=0,y=110)

options=tk.StringVar(top)
options.set()

option_selector=tk.OptionMenu()

c_stack=tk.Button(top,text="Create Stack",width=10,height=5,command=lambda:create_stack(),anchor="center")
c_stack.place(x=13,y=150)

append_stack=tk.Button(top,text="Append Stack",width=10,height=5,command=lambda:m_sele_stack.push(input_box),anchor="center")
append_stack.place(x=103,y=150)

pop_stack=tk.Button(top,text="Pop Stack",width=10,height=5,command=lambda:m_sele_stack.pop(),anchor="center")
pop_stack.place(x=203,y=150)

dis_stack=tk.Button(top,text="Display Stack",width=10,height=5,command=lambda:m_sele_stack.display(view_box),anchor="center")
dis_stack.place(x=13,y=250)

#stack_selector.place(x=103,y=250)

top.mainloop()

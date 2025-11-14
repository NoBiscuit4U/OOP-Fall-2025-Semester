import tkinter as tk
from tkinter import *

class Stack:
    def __init__(self):
        self.elements=[]
        self.text=""

    def get_elements(self):
        return self.elements

    def append(self,input_box):
        self.elements.append(str(input_box.get(1.0,"end-1c")))

    def append_val(self,val):
        self.elements.append(val)

    def remove(self):
        if len(self.elements) !=0:
            self.elements.pop()

    def display(self,dis_box):
        if len(self.elements) != 0:
            str_ele=self.elements[0]

            for element in self.elements[1:]:
                if element.__class__.__name__=="str":
                    str_ele += f",{element}"
                else:
                    if element.__class__.__name__ == "Queue":
                        str_ele += ",Queue("
                    else:
                        str_ele += ",Stack("

                    for sub_ele in element.get_elements():
                        str_ele += f"{sub_ele},"
                    str_ele = str_ele[:-1]
                    str_ele += ")"

            dis_box.delete(1.0,tk.END)
            dis_box.insert(tk.INSERT,str_ele)

class Queue:
    def __init__(self):
        self.elements=[]

    def get_elements(self):
        return self.elements

    def append(self,input_box):
        self.elements.append(str(input_box.get(1.0,"end-1c")))

    def append_val(self,val):
        self.elements.append(val)

    def remove(self):
        if len(self.elements)!=0:
            self.elements.pop(0)
        else:
            print("No Values")

    def display(self,target):
        if len(self.elements) != 0:
            str_ele = self.elements[0]

            for element in self.elements[1:]:
                if element.__class__.__name__=="str":
                    str_ele += f",{element}"
                else:
                    if element.__class__.__name__ == "Queue":
                        str_ele += ",Queue("
                    else:
                        str_ele += ",Stack("

                    for sub_ele in element.get_elements():
                        str_ele += f"{sub_ele},"
                    str_ele=str_ele[:-1]
                    str_ele+= ")"

            target.delete("1.0", tk.END)
            target.insert(tk.INSERT, str_ele)

#Main

top=tk.Tk()

m_stacks_queues=[Stack()]
m_options=["Stack 1"]

m_option_var=tk.StringVar(top)
m_option_var.set(m_options[0])

m_inherit_var=tk.StringVar(top)
m_inherit_var.set(m_options[0])

m_sele=m_stacks_queues[0]
m_sele_toi=0

option_selector=tk.OptionMenu(top,m_option_var,*m_options,command=lambda x: select("Option",x))
option_selector.pack()

merge_selector=tk.OptionMenu(top,m_inherit_var,*m_options,command=lambda y: select("Inherit",y))
merge_selector.pack()

top.geometry("500x375")
view_box=tk.Text(top,width=150,height=1)
view_box.place(x=0,y=50)
input_box=tk.Text(top,width=150,height=1)
input_box.place(x=0,y=110)

def create(key):
    global option_selector,merge_selector
    match key:
        case "Stack":
            m_stacks_queues.append(Stack())
            m_options.append(f"{key} {len(m_stacks_queues)}")

        case "Queue":
            m_stacks_queues.append(Queue())
            m_options.append(f"{key} {len(m_stacks_queues)}")

    option_selector=tk.OptionMenu(top,m_option_var,*m_options, command=lambda x: select("Option",x))
    merge_selector=tk.OptionMenu(top,m_inherit_var,*m_options,command=lambda y: select("Inherit",y))
    option_selector.place(x=30,y=270)
    merge_selector.place(x=220,y=270)

def select(key,x):
    global m_sele, m_sele_toi

    match key:
        case "Option":
            m_sele = m_stacks_queues[int(x[-1:]) - 1]
            view_box.delete(1.0, tk.END)

            if x[0:-2]=="Stack":
                append_stack.configure(text="Push")
                pop_stack.configure(text="Pop")
            else:
                append_stack.configure(text="Enqueue")
                pop_stack.configure(text="Dequeue")

        case "Inherit":
            m_sele_toi = (int(x[-1:])-1)
            print(m_sele_toi)

def inherit():
    m_stacks_queues[m_sele_toi].append_val(m_sele)

c_stack=tk.Button(top,text="Create Stack",width=10,height=5,command=lambda:create("Stack"),anchor="center")
c_stack.place(x=13,y=150)

c_stack=tk.Button(top,text="Create Queue",width=10,height=5,command=lambda:create("Queue"),anchor="center")
c_stack.place(x=103,y=150)

append_stack=tk.Button(top,text="Push",width=10,height=5,command=lambda:m_sele.append(input_box),anchor="center")
append_stack.place(x=203,y=150)

pop_stack=tk.Button(top,text="Pop",width=10,height=5,command=lambda:m_sele.remove(),anchor="center")
pop_stack.place(x=303,y=150)

dis_stack=tk.Button(top,text="Display",width=10,height=5,command=lambda:m_sele.display(view_box),anchor="center")
dis_stack.place(x=403,y=150)

option_header=tk.Label(top,text="Select Stack or Queue:",anchor="center")
option_header.place(x=13,y=250)
option_selector.place(x=30,y=270)

merge_header=tk.Label(top,text="Stack or Queue To Inherit Selected:",anchor="center")
merge_header.place(x=180,y=250)
merge_selector.place(x=220,y=270)

merge=tk.Button(top,text="Inherit",width=10,height=5,command=lambda:inherit(),anchor="center")
merge.place(x=403,y=250)

top.mainloop()
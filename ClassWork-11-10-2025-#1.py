import tkinter as tk
from tkinter import StringVar

from Tools.scripts.dutree import display
from Tools.scripts.make_ctype import values


class Queue:
    def __init__(self):
        self.elements=[]

    def enqueue(self,value):
        self.elements.append(value)
        print("enqueued", value)

    def dequeue(self):
        if len(self.elements)!=0:
            self.elements.pop(0)
        else:
            print("No Values")

    def display_queue(self,target):
        str_ele=self.elements[0]
        for element in self.elements[1:]:
             str_ele+=f",{element}"
        target.delete("1.0",tk.END)
        target.insert(tk.INSERT,str_ele)

m_queues=[Queue()]
m_queue=m_queues[0]

def create_queue():
    m_queues.append(Queue())
    print("Created Queue")

def select_queue(x,queue_select):
    global m_queue
    m_queue=x
    print("Selected Queue")


top=tk.Tk()
top.geometry("300x375")
view_box=tk.Text(top,width=150,height=1)
view_box.place(x=0,y=50)
input_box=tk.Text(top,width=150,height=1)
input_box.place(x=0,y=110)

c_queue=tk.Button(top,text="Create Queue",width=10,height=5,command=lambda:create_queue(),anchor="center")
c_queue.place(x=13,y=150)

enqueue=tk.Button(top,text="Enqueue",width=10,height=5,command=lambda:m_queue.enqueue(input_box.get(1.0,"end-1c")),anchor="center")
enqueue.place(x=103,y=150)

dequeue=tk.Button(top,text="Dequeue",width=10,height=5,command=lambda:m_queue.dequeue(),anchor="center")
dequeue.place(x=203,y=150)

dis_queue=tk.Button(top,text="Display Queue",width=10,height=5,command=lambda:m_queue.display_queue(view_box),anchor="center")
dis_queue.place(x=13,y=250)

queue_selector=tk.OptionMenu(top,value="Queue",variable=StringVar(name="Queue",value=m_queue),command=lambda x:select_queue(x,queue_selector))
queue_selector.place(x=103,y=250)

top.mainloop()



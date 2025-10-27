import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk

root=tk.Tk()
frm=tk.Frame(root)
root.resizable(False,False)
myCanvas=tk.Canvas(root,bg="white",height=500,width=800)

circle=myCanvas.create_oval(200,200,250,250,fill="red")

myCanvas.pack()
root.mainloop()


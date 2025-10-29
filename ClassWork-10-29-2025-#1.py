from tkinter import *

calc_values=["7","8","9","x",
             "4","5","6","-",
             "1","2","3","+",
             "0",".","/","="]

strt_coord=[150,150]
buttons=[]

top=Tk()
top.geometry("600x600")
top.configure(background="white")

oper_window=Text(width=100,height=50)
oper_window.place(x=100,y=100)

def show(value):
    print(value)
    try:
        if value=="=":
            ansr=eval(oper_window.get(1.0,"end-1c"))
            oper_window.insert(INSERT,value)
            oper_window.insert(INSERT,ansr)

        else:
            oper_window.insert(INSERT,value)
    except:
        oper_window.delete("1.0",END)

index=1
for i in range(len(calc_values)):
    new_button=Button(top,text=str(calc_values[i]),width=10,height=5,command=lambda:show(str(calc_values[i])))
    new_button.place(x=strt_coord[0], y=strt_coord[1])

    if index<4:
        strt_coord=[strt_coord[0]+100,strt_coord[1]]
        index+=1
    else:
        strt_coord=[150,strt_coord[1]+100]
        index=1

top.mainloop()




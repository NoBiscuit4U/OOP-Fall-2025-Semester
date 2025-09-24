options=["Stack","Destack","Print Current Stack"]
current_stack=[]

def stack(val):
    current_stack.append(val)
def destack():
    current_stack.pop()

while 1:
    for i in range(0,len(options)):
        print(i," "+options[i])

    selection=int(input("Enter Desired Option: "))

    if selection==0:
        input_val=input("Enter Value to Stack: ")
        stack(input_val)
    elif selection==1:
        destack()
    elif selection==2:
        print("Current Stack is:",current_stack)
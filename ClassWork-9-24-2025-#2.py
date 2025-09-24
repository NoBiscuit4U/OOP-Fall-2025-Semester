options=["Enqueue","Dequeue","Print Current Queue"]
current_queue=[]

def enqueue(val):
    current_queue.append(val)
def dequeue():
    current_queue.pop(0)

while 1:
    for i in range(0,len(options)):
        print(i," "+options[i])

    selection=int(input("Enter Desired Option: "))

    if selection==0:
        input_val=input("Enter Value to Queue: ")
        enqueue(input_val)
    elif selection==1:
        dequeue()
    elif selection==2:
        print("Current Queue is:",current_queue)
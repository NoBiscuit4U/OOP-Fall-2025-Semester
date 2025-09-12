options=["Add Elements","Remove All Of Specific Elements","Replace Element","Sort List","Reverse List","Display List","Quit"]
list=[]
user_input=[]
index=0

while True:
    print("-------")
    print("Options")
    for i in range(0,len(options)):
        print(i," "+options[i])

    selection=int(input("Enter Desired Option: "))

    if selection == 2:
        user_input = input("Enter Element: ")
        index=int(input("Enter Index: "))
    elif selection < 2:
        user_input=input("Enter Elements seperated by comma: ").split(",")

    if selection == 0:
        for element in user_input:
            list.append(element)
    elif selection == 1:
        for element in user_input:
            if element in list:
                list.remove(element)
            else:
                print("Element: -",element,"- Not In List")
    elif selection == 2:
        if index < len(list):
            list[index]=user_input
    elif selection == 3:
        list.sort()
    elif selection == 4:
        list.reverse()
    elif selection == 5:
        print("Current List: ",list)
    elif selection == 6:
        print("Exiting Program")
        break
    else:
        print("Not Valid Option")
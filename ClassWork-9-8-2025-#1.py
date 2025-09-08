options=["Add Elements","Remove All Of Specific Elements","Pop Element","Display List","Quit"]
list=[]
elements=[]
index=0

while True:
    print("-------")
    print("Options")
    for i in range(0,len(options)):
        print(i," "+options[i])

    selection=int(input("Enter Desired Option: "))

    if selection < 2:
        elements=input("Enter Elements seperated by comma: ").split(",")
    elif selection < 3:
        index=int(input("Enter Index: "))

    if selection == 0:
        for element in elements:
            list.append(element)
    elif selection == 1:
        for element in elements:
            if element in list:
                list.remove(element)
            else:
                print("Element: -",element,"- Not In List")
    elif selection == 2:

        if index < len(list):
            pop_value=list.pop(index)
            print("Popped Element: ",pop_value)

    elif selection == 3:
        print("Current List: ",list)

    elif selection == 4:
        print("Exiting Program")
        break
    else:
        print("Not Valid Options")

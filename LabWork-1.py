while True:
    operation_options=["Addition","Subtraction","Multiplication","Division","Quit"]

    for i in range(0,len(operation_options)):
        print(i,". "+operation_options[i])

    option=input("Enter Desired Option: ")

    if option !="4":
        numbers = input("Enter Two Numbers Seperated by a ,: ").split(",")
    else:
        break

    if option=="0":
        print(numbers[0]+" + "+numbers[0]," = ",int(numbers[0])+int(numbers[1]))
    elif option=="1":
        print(numbers[0]+" - "+numbers[0]," = ",int(numbers[0])-int(numbers[1]))
    elif option=="2":
        print(numbers[0]+" * "+numbers[0]," = ",int(numbers[0])*int(numbers[1]))
    elif option=="3":
        print(numbers[0]+" / "+numbers[0]," = ",int(numbers[0])/int(numbers[1]))
    else:
        print("Invalid Option Chosen")

print("Application Exited")


while True:
    operation_options=["Addition","Subtraction","Multiplication","Division","Quit"]

    for i in range(0,len(operation_options)):
        print(i,". "+operation_options[i])

    option=input("Enter Desired Option: ")

    if option !="4":
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
    else:
        break

    if option=="0":
        print(a," + ",b," = ",a+b)
    elif option=="1":
        print(a, " - ", b, " = ", a-b)
    elif option=="2":
        print(a, " * ", b, " = ", a*b)
    elif option=="3":
        print(a, " / ", b, " = ", a/b)
    else:
        print("Invalid Option Chosen")

print("Application Exited")


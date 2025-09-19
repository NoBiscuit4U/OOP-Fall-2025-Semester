myEmployees={}
employee_template={"Name":"","Pay":"","Allowance":"","Deductions":"","Taxes":""}
options=["Add an Employee","Delete an Employee","Modify Employee Information","Display Employee Information","Exit Program"]

while True:
    print("-------")
    employee_name=""
    user_input=""

    for i in range(0,len(options)):
        print(i," "+options[i])

    selected=int(input("Enter the Number of Desired Option: "))

    if selected == 0:
        user_input=input("Enter The Employee Information: Name,Pay,Allowance,Deductions,Taxes: ").split(",")
        
        gross_pay = int(user_input[1]) + int(user_input[2])
        net_pay= gross_pay-(int(user_input[3])+int(user_input[4]))
        new_employee={"Employee-"+str(len(myEmployees)):{
            "Name": user_input[0],
            "Pay": user_input[1],
            "Allowance": user_input[2],
            "Deductions": user_input[3],
            "Taxes": user_input[4],
            "GrossPay": str(gross_pay),
            "NetPay": str(net_pay)
        }}

        myEmployees.update(new_employee)
    elif selected == 1:
        employee_name=input("Enter The Employee Name for Removal: ")
        
        for key in myEmployees.keys():
            if myEmployees[key].get("Name") == employee_name:
                del myEmployees[key]
                break

    elif selected == 2:
        user_input = input("Enter The New Information: Name,Pay,Allowance,Deductions,Taxes: ").split(",")
        
        for key in myEmployees.keys():
            if myEmployees[key].get("Name") == user_input[0]:
                index = 0
                gross_pay = int(user_input[1]) + int(user_input[2])
                net_pay= gross_pay-(int(user_input[3])+int(user_input[4]))
                for info_key in employee_template:
                    myEmployees[key].update({info_key: user_input[index]})
                    index += 1
                myEmployees[key].update({"GrossPay":str(gross_pay)})
                myEmployees[key].update({"NetPay": str(net_pay)})

    elif selected == 3:
        print("-----")
        print("Employee Information: ")
              
        for info in myEmployees.items():
            print(info)
        
        print("-----")

    elif selected == 4:
        print("Exiting Program")
        break
    else:

        print("Invalid Option")



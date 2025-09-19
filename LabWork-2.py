myEmployees={}
employee_template={"Name":"","Pay":"","Allowance":"","Deductions":"","Taxes":"","GrossPay":"","NetPay":""}
employee_calc_values={"GrossPay":"","NetPay":""}
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
    elif selected == 1:
        employee_name=input("Enter The Employee Name for Removal")
    elif selected == 2:
        user_input = input("Enter The New Information: Name,Pay,Allowance,Deductions,Taxes: ").split(",")

    if selected == 0:
        gross_pay = int(user_input[1]) + int(user_input[2])
        net_pay= int(gross_pay-(int(user_input[3])+int(user_input[4])))
        new_employee={user_input[0]:{
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
            if employee_name in myEmployees.keys():
                del myEmployees[employee_name]
    elif selected == 2:
        for key in myEmployees:
            if key == employee_name:
                gross_pay = int(user_input[1] + user_input[2])
                net_pay = int(gross_pay - (int(user_input[3]) + int(user_input[4])))
                for info_key in myEmployees[key]:
                    i = 0
                    myEmployees[key].update({info_key: user_input[i]})
                    i += 1
                myEmployees[key].update({"GrossPay":str(gross_pay)})
                myEmployees[key].update({"NetPay": str(net_pay)})

    elif selected == 3:
        for info in myEmployees.items():
            print("-----")
            print("Employee Information: ",info)
            print("-----")

    elif selected == 4:
        print("Exiting Program")
        break
    else:
        print("Invalid Option")
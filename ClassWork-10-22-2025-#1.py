from unittest import case


class Customer:
    def __init(self):
        self.c_id=""
        self.name=""
        self.acc_num=""
        self.phone=""
        self.email=""
        self.balance=0

    def add_attributes(self):
        vals = input("Enter Values for: ID,Name,AccountNumber,Phone,Email,Balance: ").split(",")

        self.c_id=vals[0]
        self.name=vals[1]
        self.acc_num=vals[2]
        self.phone=vals[3]
        self.email=vals[4]
        self.balance=int(vals[5])

    def edit_values(self,key,val):
        match key.lower():
            case "id":
                self.c_id=val
            case "name":
                self.name=val
            case "accountnumber":
                self.acc_no=val
            case "phone":
                self.phone=val
            case "email":
                self.email=val
            case "balance":
                self.balance=val
            case _:
                print("Invalid Key")

    def deduct_balance(self,amount):
        self.balance-=amount

    def increment_balance(self,amount):
        self.balance+=amount

    def display_info(self):
        prin_vals={"ID":self.c_id,"Name":self.name,"AccountNumber":self.acc_num,"Phone":self.phone,"Email":self.email,"Balance":self.balance}

        print(f"    Customer-{self.c_id} Info: ")
        for key in prin_vals:
            print(f"        {key}: {prin_vals[key]}")

#Main
customers={}
options=["Create Customer","Remove Customer","Edit Customer Values","Display All Customer Information","Money Transfer","Exit"]

while 1:

    print("Options:")
    for i in range(len(options)):
        print(f"    {options[i]}: {i}")

    select=int(input("Select Option: "))

    match select:
        case 0:
            new_c=Customer()
            new_c.add_attributes()

            customers.update({f"{new_c.c_id}":new_c})
        case 1:
            id_remove=int(input("Enter ID of Customer to Remove: "))

            del customers[f"{id_remove}"]
        case 2:
            c_id=int(input("Enter Customer ID"))
            edit_key=input("Enter Key of Value To Edit: ")
            edit_val = input("Enter Value: ")

            for customer in customers:
                if customer.c_id==c_id:
                    customer.edit_values(edit_key,edit_val)

        case 3:
            print("All Customer Information: ")

            for customer in customers.values():
                customer.display_info()

        case 4:
            ded_c_id=(input("Enter Customer ID for Deduction: "))
            inc_c_id=(input("Enter Customer ID for Incrementation: "))
            amnt=int(input("Enter Amount: "))

            customers[ded_c_id].deduct_balance(amnt)
            customers[inc_c_id].increment_balance(amnt)

        case 5:
            print("Exiting")
            break

        case _:
            print("Invalid Selection")


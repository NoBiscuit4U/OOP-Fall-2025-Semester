import pickle

class Card:
    def __init__(self,crd_type):
        self.crd_type=crd_type
        self.card_num=""
        self.cvv=""
        self.expir_date=""
        self.balance=0

    def add_attributes(self):
        vals=input("Enter Values for: CardNumber,CVV,ExpirationDate,Balance: ").split(",")

        self.card_num=vals[0]
        self.cvv=vals[1]
        self.expir_date=vals[2]
        self.balance=float(vals[3])

    def display_info(self):
        prin_vals={"Type": self.crd_type,"Card Number": self.card_num,"Expiration Date": self.expir_date,"Balance": self.balance}

        print(f"            Card-{self.card_num} Info: ")
        for key in prin_vals:
            print(f"                    {key}: {prin_vals[key]}")

class Customer:
    def __init(self):
        self.c_id=""
        self.name=""
        self.acc_num=""
        self.phone=""
        self.email=""
        self.balance=0
        self.credit_cards=[]
        self.debit_card=""

    def add_attributes(self):
        vals = input("Enter Values for: ID,Name,AccountNumber,Phone,Email,Balance: ").split(",")

        self.c_id=vals[0]
        self.name=vals[1]
        self.acc_num=vals[2]
        self.phone=vals[3]
        self.email=vals[4]
        self.balance=float(vals[5])
        self.credit_cards = []
        self.debit_card = ""

    def add_card(self,card):
        if card.crd_type=="Credit":
            self.credit_cards.append(card)
        else:
            self.debit_card=card

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
        prin_vals={"ID":self.c_id,"Name":self.name,"AccountNumber":self.acc_num,"Phone":self.phone,"Email":self.email,"Balance":self.balance,"Credit Cards":self.credit_cards,"Debit Card":self.debit_card}

        print(f"    Customer-{self.c_id} Info: ")
        for key in prin_vals:
            if key == "Credit Cards":
                print("         Credit Cards")
                for card in prin_vals[key]:
                    card.display_info()
            elif key == "Debit Card":
                 print("         Debit Card")
                 if prin_vals[key] != "":
                     prin_vals[key].display_info()
            else:
                print(f"        {key}: {prin_vals[key]}")

#Main
customers={}
options=["Create Customer","Remove Customer","Edit Customer Values","Add Card to Customer","Display All Customer Information","Money Transfer","Write Values","Exit"]
wr_fp="customer_info.dat"

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
            cstr_id = input("Enter Customer ID: ")
            crd_type=input("Enter Card Type: ")

            match crd_type.lower():
                case "credit":
                    n_card = Card(crd_type)
                    n_card.add_attributes()
                case "debit":
                    n_card = Card(crd_type)
                    n_card.add_attributes()
                case _:
                    print("Invalid Card Type")
                    break

            for key in customers.keys():
                if customers[key].c_id==cstr_id:
                    customers[key].add_card(n_card)
                    break
        case 4:
            print("All Customer Information: ")

            for customer in customers.values():
                customer.display_info()

        case 5:
            ded_c_id=(input("Enter Customer ID for Deduction: "))
            inc_c_id=(input("Enter Customer ID for Incrementation: "))
            amnt=int(input("Enter Amount: "))

            customers[ded_c_id].deduct_balance(amnt)
            customers[inc_c_id].increment_balance(amnt)

        case 6:
            with open(wr_fp,"wb") as f:
                pickle.dump(customers,f)

            f.close()

            print(f"{len(customers)} Customers Written to File")

        case 7:
            print("Exiting")
            break

        case _:
            print("Invalid Selection")


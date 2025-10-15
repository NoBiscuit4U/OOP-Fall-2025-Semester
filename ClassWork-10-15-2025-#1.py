import pickle

class Product:
    def __init__(self):
        product_details=input("Enter Product Details: ID,Name,Price: ").split(",")
        self.pid=product_details[0]
        self.name=product_details[1]
        self.price=product_details[2]

    def get_product_details(self):
        details = {"ID": self.pid, "Name": self.name, "Price": self.price}

        key=input("Enter Desired Info: ID, Name, Price: ")

        if key in details.keys():
            print(f"{key}: {details[key]}")
            return details[key]
        else:
            print("Attribute Doesnt Exist")
            return None

    def display_product_details(self):
        details={"ID": self.pid,"Name": self.name,"Price": self.price}

        print(f"Product ID {self.pid}")
        for key in details:
            print(f"    {key}: {details[key]}")

options=["Create Product","Get Information for the Product","Display the Product","Write Product to File","Read and Display Product Information"]
product=""

while 1:
    print("Available Options")

    for i in range(len(options)):
        print(f"    {i}: {options[i]}")

    selection=int(input("Select Option: "))

    if selection==0:
        product=Product()

    elif selection==1:
        product.get_product_details()

    elif selection==2:
        product.display_product_details()

    elif selection==3:
        with open("product_information","ab") as f:
            pickle.dump(product,f)

        f.close()
    elif selection==4:
        with open("product_information","rb") as f:
            while 1:
                try:
                    r_pdct=pickle.load(f)
                    r_pdct.display_product_details()
                except:
                    print("End of File Reached")
                    break
        f.close()
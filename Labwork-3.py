class Book:
    def __init__(self,id,title,author):
        self.bookInfo={
            "ID": id,
            "Title": title,
            "Author": author
        }
    
    def get_book_info(self,key=""):
        if key in self.bookInfo.keys():
            return self.bookInfo[key]
        else:
            return self.bookInfo
        
    def edit_book_info(self):
        key=input("Desired Key to Edit: ")
        value=input("Input Value for Key : ")
        self.bookInfo[key]=value
    
    def display_book_info(self):
        print("Book Information: ")
        for key in self.bookInfo.keys():
            print(f"{key}: ",self.bookInfo[key])

class User:
    def __init__(self,id,name):
        self.userInfo={
            "ID": id,
            "Name": name,
            "BooksBorrowed": []
        }
    
    def get_user_info(self,key=""):
        if key in self.userInfo.keys():
            return self.userInfo[key]
        else:
            return self.userInfo
        
    def edit_user_info(self):
        key=input("Desired Key to Edit: ")
        value=input("Input Value for Key : ")
        self.userInfo[key]=value
    
    def add_book(self,book):
        self.userInfo["BooksBorrowed"].append(book)
    
    def display_user_info(self):
        print("User Info: ")
        for key in self.userInfo.keys():
            if key == "BooksBorrowed":
                print("Book Information: ")
                for book in self.userInfo[key]:
                    book_info=book.get_book_info()
                    print("    Book: "+book_info["Title"])
                    for ckey in book_info.keys():
                        print(f"        {ckey}: ", book_info[ckey])
            else:
                print(f"    {key}: ", self.userInfo[key])


# Main
books=[
    Book("001","Virtuous Minds","Philip Dow"),
    Book("002","The Art of War","Sun Tzu"),
    Book("003","Calculus1","Bluma"),
    Book("004","Calculus2","Bluma"),
    Book("005","Calculus3","Bluma"),
]

user1=User("101","Dan")
user2=User("102","John")

for book in books:
    user1.add_book(book)
    user2.add_book(book)

user1.display_user_info()
user2.display_user_info()
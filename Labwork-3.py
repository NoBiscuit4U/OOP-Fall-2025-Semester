class Book:
    def __init__(self, book_id, title, author_id, publisher, year_publication):
        self.bookInfo = {
            "ID": book_id,
            "Title": title,
            "Author ID": author_id,
            "Publisher": publisher,
            "Year of Publication": year_publication
        }

    def get_book_info(self, key=""):
        if key in self.bookInfo.keys():
            return self.bookInfo[key]
        else:
            return self.bookInfo

    def edit_book_info(self,info_key,value):
        self.bookInfo[info_key] = value

    def display_book_info(self):
        print(f"Book-{self.bookInfo['ID']} Information: ")
        for key in self.bookInfo.keys():
            print(f"{key}: ", self.bookInfo[key])

class Author:
    def __init__(self, author_id, name, affiliation, country, phone, email):
        self.authorInfo = {
            "ID": author_id,
            "Name": name,
            "Affiliation": affiliation,
            "Country": country,
            "Phone": phone,
            "Email": email
        }

    def get_author_info(self, key=""):
        if key in self.authorInfo.keys():
            return self.authorInfo[key]
        else:
            return self.authorInfo

    def edit_author_info(self,info_key,value):
        self.authorInfo[key] = value

    def display_author_info(self):
        print(f"Author-{self.authorInfo['ID']} Information: ")
        for key in self.authorInfo.keys():
            print(f"{key}: ", self.authorInfo[key])


class User:
    def __init__(self, user_id, name, password, address, phone, email):
        self.userInfo = {
            "ID": user_id,
            "Name": name,
            "Password": password,
            "Address": address,
            "Phone": phone,
            "Email": email,
            "BooksBorrowed": []
        }

    def get_user_info(self, key=""):
        if key in self.userInfo.keys():
            return self.userInfo[key]
        else:
            return self.userInfo

    def edit_user_info(self,info_key,value):
        self.userInfo[info_key] = value

    def add_book(self, book):
        self.userInfo["BooksBorrowed"].append(book)

    def display_user_info(self):
        print(f"User-{self.userInfo['ID']} Information: ")
        for key in self.userInfo.keys():
            if key == "BooksBorrowed":
                print("Book Information: ")
                for book in self.userInfo[key]:
                    book_info = book.get_book_info()
                    print("    Book: " + book_info["Title"])
                    for ckey in book_info.keys():
                        print(f"        {ckey}: ", book_info[ckey])
            else:
                print(f"    {key}: ", self.userInfo[key])

# Main
options=["Create User","Create Book","Create Author","Lend Book","Display Users","Display Books","Display Authors","Quit"]
books=[]
users=[]
authors=[]

while 1:
    for i in range(0,len(options)):
        print(f"{i}: {options[i]}")

    selection=int(input("Select an Operation: "))

    if selection == 0:
        new_user=User("","","","","","")

        for key in new_user.get_user_info().keys():
            if key != "BooksBorrowed":
                new_user.edit_user_info(key, input(f"Input value for {key}: "))

        users.append(new_user)

    elif selection == 1:
        new_book = Book("", "", "", "", "")

        for key in new_book.get_book_info().keys():
            new_book.edit_book_info(key, input(f"Input value for {key}: "))

        books.append(new_book)

    elif selection == 2:
        new_author = Author("", "", "", "", "","")

        for key in new_author.get_author_info().keys():
            new_author.edit_author_info(key, input(f"Input value for {key}: "))

        authors.append(new_author)

    elif selection == 3:
        user_id=input("Enter User ID: ")
        book_id=input("Enter Book ID:")

        for user in users:
            if user.userInfo["ID"] == user_id:
                for book in books:
                    if book.get_book_info("ID") == book_id:
                        user.add_book(book)
                        break
                break

    elif selection == 4:
        print("All User Information:")
        for user in users:
            user.display_user_info()

    elif selection == 5:
        print("All Book Information:")
        for book in books:
            book.display_book_info()

    elif selection == 6:
        print("All Author Information:")
        for author in authors:
            author.display_author_info()

    elif selection == 7:
        print("Quitting Program")

    else:
        print("Invalid Option")

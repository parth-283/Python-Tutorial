"""
Create a Library Class
Display book
Land Book
Add Book
Return Book
PRLibrary = Library(listofbook, library_name)
dictionary (books-nameofperson)
create a mian function and run an infinite while loop asking users for their input
"""
import datetime
from builtins import print

book_in_libary = ["The Forest of Hands and Teeth", "Something Wicked This Way Comes", "Where the Sea Breaks Its Back",
                  "Wuthering Heights"]
client_account = {}


class Library:

    def __init__(self, book_name):
        self.book_name = book_name

    def display(self):
        return f"Library {self.book_name}"

    def add_books(self):
        book_in_libary.append(self.book_name)

    def remove(self):
        book_in_libary.remove(self.book_name)


Library_Service = {1: "List of book", 2: "take Books", 3: "Donate Book", 4: "Return Book"}

print(" Welcome to my library ")


while True:
    dateAndTime = datetime.datetime.now()
    date = dateAndTime.strftime("%d/%m/%y")
    time = dateAndTime.strftime("%I:%M %p")
    user_Choose_Service1 = int(input(f"{Library_Service}\nSelect One : "))
    user_Choose_Service2 = Library_Service[user_Choose_Service1]

    if user_Choose_Service2 == "List of book":
        i = 0
        for books in book_in_libary:
            i += 1
            print(f"{i} {books}")

    elif user_Choose_Service2 == "take Books":

        client_name = input("Enter your name : ")
        take_book_name = input("Enter book name : ")
        if take_book_name in book_in_libary:
            if client_name in client_account:
                client_account[client_name].append({take_book_name, date, time})
                book_in_libary.remove(take_book_name)
                print("Book send to in your account", client_account)
            else:
                client_account.update({client_name: [{take_book_name, date, time}]})
                book_in_libary.remove(take_book_name)
                print("Book send to in your account", client_account)
        else:
            print(f"{book_in_libary} Only those books in present")

    elif user_Choose_Service2 == "Donate Book":

        donate_book_name = input(f"Enter your book name : ")
        client = Library(donate_book_name)
        Library(client.add_books())
        print("Donate Book")

    elif user_Choose_Service2 == "Return Book":

        client_name = input("Enter your name : ")
        return_book_name = input("Enter book name : ")
        if client_name in client_account:
            for i in range(len(client_account[client_name])):
                if return_book_name in client_account[client_name][i]:
                    client = Library(return_book_name)
                    Library(client.add_books())
                    client_account[client_name].remove(client_account[client_name][i])
                    if client_account[client_name] == set():
                        print(f"you return : {return_book_name} ")
                    else:
                        print(f"you take : {client_account[client_name]}, you return : {return_book_name} ")
                    print("Book remove to in your account and submit to library ")
                    break

            else:
                print("Book not found")
        else:
            print("Client not found")

    else:

        print("Enter Right Number")

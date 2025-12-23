
from library_system.library import Library
from library_system.book import Book
from library_system.member import Member

lib = Library()

while True:
    print("\n1.Add Book 2.Register Member 3.Borrow 4.Return 5.View 6.Exit")
    c = input("Choice: ")
    if c=="1":
        lib.add_book(Book(input("Title:"),input("Author:"),input("ISBN:"),input("Year:")))
    elif c=="2":
        lib.register_member(Member(input("Name:"),input("Member ID:")))
    elif c=="3":
        print("Success" if lib.borrow_book(input("ISBN:"),input("Member ID:")) else "Failed")
    elif c=="4":
        print("Returned" if lib.return_book(input("ISBN:"),input("Member ID:")) else "Failed")
    elif c=="5":
        for b in lib.books.values():
            print(b.title, b.author, "Available" if b.available else "Borrowed")
    elif c=="6":
        lib.save_data()
        break

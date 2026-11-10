from printer import *
from librarian import *

while True:

    choose = print_menu()

    if choose == "1":
        display_books()

    if choose == "2":
        print(search_book())

    if choose == "3":
        add_book()

    if choose == "4":
        borrow_book()

    if choose == "5":
        return_book()

    if choose == "6":
        get_available_books()

    if choose == "7":
        get_books_by_author()

    if choose == "8":
        print("bye")
        break

    else:
        print("enter number between 0 - 7 or  8 to exit: ")

from data import books_data

def str_to_int(num):
    try:
        num = int(num)
        return num
    except:
        return 0


def is_valid_name(name):
    if len(name.strip()) != 0:
        return False
    return True


def is_exist_name(check, name):
    for book in books_data:
        if book[check] == name:
            return True
        return False


def get_name():
    name = input("enter a name book: ")
    while is_valid_name(name) or is_exist_name("name", name):
        name = input("enter a name book: ")
    return name


def get_author():
    author = input("enter a author name: ")
    while is_valid_name(author) or is_exist_name("author", author):
        author = input("enter a author name: ")
    return author


def get_year():
    year = input("enter a year: ")
    while str_to_int(year) == 0 or not 0 < str_to_int(year) < 2026:
        year = input("enter a year: ")
    return year


def get_next_book_id():
    return len(books_data) + 1


def is_id_exist_and_available(action):
    id_book = input("Enter id num: ")
    if 0 < str_to_int(id_book) <= len(books_data):
        for book in books_data:
            if book["id"] == int(id_book):
                if action == "borrow":
                    if book["available"] is True:
                        book["available"] = False
                    else:
                        print("The book is on loan.")
                if action == "return":
                    if not book["available"]:
                        book["available"] = True
                    else:
                        print("The book is not for loan.")
    print("the book not exist")


def is_book_exist():
    name = get_name()
    for book in books_data:
        if name == book["name"]:
            return book
    return None

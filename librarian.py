# from .data import books_data
from validation import *


def display_books():
    print(books_data)


def search_book():
    return is_book_exist()


def add_book():
    books_data.append({"id": get_next_book_id(), "name": get_name(), "author": get_author(), "year": get_year(), "available": True})


def borrow_book():
    return is_id_exist_and_available("borrow")


def return_book():
    return is_id_exist_and_available("return")


def get_available_books():
    print(list(filter(lambda b:b["available"] is True, books_data)))


def get_books_by_author():
    name = get_author()
    print(list(filter(lambda b:b["author"] == name, books_data)))
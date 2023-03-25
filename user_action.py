import file_io
import re


def add_new_book(filename, books):
    """Converts a book info entered by the user into a dictionary, adds it to the book list and saves the list to a
    json file."""

    title = input("Enter Title of the Book: ")
    if re.search("^[a-zA-Z0-9 ]+$", title) is None:
        raise ValueError("Book Name is invalid")

    author = input("Enter Author of the Book: ")
    if re.search("^[a-zA-Z ]+$", author) is None:
        raise ValueError("Author Name is invalid")

    year = input("Enter year of the Book: ")
    if re.search("^\d{4}$", year) is None:
        raise ValueError("Year must be four digits.")
    if int(year) < 1901:
        raise ValueError("Year should be greater than 1900.")

    isbn = input("Enter ISBN of the Book: ")
    if re.search("^\d{4,18}$", isbn) is None:
        raise ValueError("ISBN is invalid.")
    for book in books:
        if isbn == book["ISBN"]:
            raise ValueError("ISBN already exists, enter a unique one.")

    description = input("Enter description of the Book: ")
    if re.search("^.{1,128}$", description) is None:
        raise ValueError("Description should between 1 and 128 characters.")

    book = {"Title": title, "Author": author, "Year": year, "ISBN": isbn, "Description": description}
    books.append(book)
    file_io.save_data_to_file(filename, books)


def delete_book(filename, books):
    """Deletes a book by the book's ISBN."""

    isbn = input("Please, enter ISBN of the Book you would like to delete: ")
    if re.search("^\d{4,18}$", isbn) is None:
        raise ValueError("ISBN is invalid.")

    matches_found = False

    for book in books:
        if isbn == book["ISBN"]:
            title = book["Title"]
            books.remove(book)
            file_io.save_data_to_file(filename, books)
            print("A book titled \"%s\" has been successfully deleted." % title)
            matches_found = True
            break

    if not matches_found:
        print(f"The book with the ISBN {isbn} was not found.")


def book_summary(books):
    """Displays information for each book in the inventory to the console."""

    for book in books:
        print("Title: %s/Author: %s/Year: %s/ISBN: %s/Description: %s" % (book["Title"],
                                                                          book["Author"],
                                                                          book["Year"],
                                                                          book["ISBN"],
                                                                          book["Description"][0:30]))


def search_book_by_title(books):
    """Displays book details found by a given title."""

    title = input("Enter the title of the book to search on: ")
    if re.search("^[a-zA-Z0-9 ]+$", title) is None:
        raise ValueError("Title is invalid.")

    matches_found = False

    for book in books:
        if re.search(title.lower(), book["Title"].lower()):
            print("Title: %s/Author: %s/Year: %s/ISBN: %s/Description: %s" % (book["Title"],
                                                                              book["Author"],
                                                                              book["Year"],
                                                                              book["ISBN"],
                                                                              book["Description"]))

            matches_found = True

    if not matches_found:
        print("No matches for the current title")


def search_book_by_author(books):
    """Displays book details found by a given author."""

    author = input("Enter the author of the book to search on: ")
    if re.search("^[a-zA-Z ]+$", author) is None:
        raise ValueError("Author is invalid.")

    matches_found = False

    for book in books:
        if re.search(author.lower(), book["Author"].lower()):
            print("Title: %s/Author: %s/Year: %s/ISBN: %s/Description: %s" % (book["Title"],
                                                                              book["Author"],
                                                                              book["Year"],
                                                                              book["ISBN"],
                                                                              book["Description"]))

            matches_found = True

    if not matches_found:
        print("No matches for the current author")


def search_book_by_keyword(books):
    """Displays book details found by a given keyword."""

    keyword = input("Enter the keyword for the book to search on: ")
    if re.search("^.{1,18}$", keyword) is None:
        raise ValueError("Keyword is invalid.")

    matches_found = False

    for book in books:
        searched_parts = book["Title"] + book["Description"]
        if re.search(keyword, searched_parts):
            print("Title: %s/Author: %s/Year: %s/ISBN: %s/Description: %s" % (book["Title"],
                                                                              book["Author"],
                                                                              book["Year"],
                                                                              book["ISBN"],
                                                                              book["Description"]))

            matches_found = True

    if not matches_found:
        print("No matches for the current keyword.")

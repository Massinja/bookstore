import re
import sys
import os

import file_io
import user_action


def main():
    """Asks a user for an input to add, delete and search for books. Stores data in json file. Handles exceptions."""

    if len(sys.argv) > 2:
        print("Too many arguments to the program. It only needs two.")
        exit(0)

    elif len(sys.argv) < 2:
        print("Not enough arguments to the program. It needs the filename.")
        exit(0)

    filename = sys.argv[1]

    if os.path.isfile(filename):
        books = file_io.load_file_data(filename)

    else:
        print("The bookstore database does not exist.")
        books = []

    quit = False

    while not quit:

        option = input("Enter an action - Add a Book (a), Delete a Book (d), View Book Summary (s), Search by Title (t), Search by Author (u), Search by Keyword (k), Quit (q): ")
        if books == []:
            if re.search("^[dstuk]$", option):
                print("The bookstore is empty. Add some books first.")
                continue

        try:
            if option == "a":
                user_action.add_new_book(filename, books)

            elif option == "d":
                user_action.delete_book(filename, books)

            elif option == "s":
                user_action.book_summary(books)

            elif option == "t":
                user_action.search_book_by_title(books)

            elif option == "u":
                user_action.search_book_by_author(books)

            elif option == "k":
                user_action.search_book_by_keyword(books)

            elif option == "q":
                print("Quitting the bookstore.")
                quit = True

            else:
                print("Invalid Option Entered")

        except ValueError as e:
            print("Error: %s" % (str(e)))
        except:
            print("Something went wrong and I didn't foresee this. I must be tired.")


if __name__ == "__main__":
    main()

# Welcome to My Bookstore
***

## Description
A simple Bookstore application that allows a user to:
* Add a new book
* Delete an existing book
* View a listing of all books
* Search for the listing of a specific book (by title, author or keyword)

Files:  
**bookstore.py** – main script for the bookstore, has main() function.  
**file_io.py** - module to read/write books from file in json format and convert it between json and a Python list of dictionaries.  
**user_action.py** - module to handle each of the User Actions.

The inventory of books  must be stored in a .json file (i.e., bookstore.json) - User specifies the name when running program.  
The .json file contains a list of dictionaries where each dictionary represents the book and has the following key/value pairs:
* title
* author
* year
* isbn
* description

### **User Actions**  
The user will be prompted to perform one of the following actions:
* Add Book (a)
* Delete Book (d)
* View Book Summary (s)
* Search Book by Title (t)
* Search Book by Author (u)
* Search Book by Keyword (k)
* Quit (q)
The user will be continually prompted for the above options until the Quit (q) option is selected.

**Add Book Action**  
The user will be prompted for the following information:
* Title – letters (upper and lower), digits and spaces.
* Author – letters (upper and lower) and spaces
* Year – Four digits and greater than 1900.
* ISBN – Four to eighteen (inclusive) AND must be unique (no other
books can have this ISBN).
* Description – Any character up to 128 characters in length.

## Usage
The bookstore.py script takes one command line argument containing the filepath of the json file, for example:
```
python bookstore.py file.json
```

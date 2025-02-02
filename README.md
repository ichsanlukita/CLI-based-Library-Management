Library Management CLI (Simulation Game)

Overview

This project is a Library Management System implemented as a Command-Line Interface (CLI) simulation game. It is not a real application but a demonstration of my ability to code in Python. The purpose of this project is to showcase my programming skills in handling user input, data storage, and implementing CRUD (Create, Read, Update, Delete) operations.

Features

1. User Roles

System Administrator (Librarian): Full control over the system, including book management and user transactions.

Library Visitor: Limited access to view, borrow, and return books.

2. Book Management

View Books: List all available books or search by book ID.

Add Books: Librarians can add new books with ID, title, year, author, and stock information.

Edit Books: Update book details such as ID, title, year, author, and stock.

Delete Books: Remove books from the system.

3. Borrow & Return System

Borrow Books: Check availability and borrow a book, reducing stock accordingly.

Return Books: Increase stock upon book return.

4. Authentication

Users choose their role upon login (Admin or Visitor).

Access to features is based on role permissions.

Installation & Usage

Prerequisites

Python 3.x

Running the Application

Clone the repository or download the script.

Open a terminal or command prompt.

Navigate to the directory where the script is saved.

Run the script using:

python Simple_LibraryManagement_CLI.py

Follow the on-screen instructions to log in and navigate the menu options.

Menu Navigation

Login Page

1: Login as System Administrator (Librarian)

2: Login as Library Visitor

3: Exit

System Administrator Menu

1: View Book Availability

2: Add New Book

3: Edit Book Information

4: Delete Book

5: Borrow Book

6: Return Book

7: Exit

Library Visitor Menu

1: View Book Availability

2: Borrow Book

3: Return Book

4: Exit

Code Structure

Global Variables: Stores book data and login status.

Menu Functions: Manage user inputs and navigation.

Helper Functions: Perform specific tasks such as searching, updating, and validating book records.

Example Book Data

list_book = [
    {'ID':'001', 'Title':'Doraemon', 'Year':'1980', 'Author':'Nobita', 'Stock':2},
    {'ID':'002', 'Title':'NatGeo', 'Year':'1976', 'Author':'Johnson', 'Stock':1},
    {'ID':'003', 'Title':'Product Book', 'Year':'2000', 'Author':'Product', 'Stock':5},
]

Future Enhancements

Implement a database for persistent storage.

Add user authentication with username and password.

Enhance user interface with a graphical UI.

Author

Muhammad Ichsan Lukita


# Muhammad Ichsan Lukita 
# Library Management Application

# Orginal data of book availibility
list_book = [
        {'ID':'001', 'Title':'Doraemon', 'Year':'1980', 'Author':'Nobita', 'Stock':2 },
        {'ID':'002', 'Title':'NatGeo', 'Year':'1976', 'Author':'Johnson', 'Stock':1 },
        {'ID':'003', 'Title':'Product Book', 'Year':'2000', 'Author':'Product', 'Stock':5},
]

# List Menu in View Page
viewOptionMenu = ('''
    View Page:
    1. Show all book
    2. Find book by ID
    3. EXIT
''')
                  
# List Menu in Add Book Page

addBook_OptionMenu = ('''
    Add Book Page:
    1. Add New Book
    2. EXIT
''')

# List Menu in Edit Book Page                      
updateBook_OptionMenu = ('''
    Edit Book Page:
    1. Update information
    2. EXIT
''')
                  
updateBook_DetailInformation =('''
    Update Book Detail Information:
    1. Book ID
    2. Title
    3. Year
    4. Author
    5. Stock
    6. Cancel
''')

# List Menu in Delete Page                           
deleteBook_OptionMenu =('''
    Delet Book Page:
    1. Delete book
    2. EXIT
''')
                        
# List Menu in Borrow Page
borrowBook_OptionMenu = ('''
    Borrow Book Page:
    1. Borrow Book
    2. Cancel
''')

# List Menu in Return Page
returnBook_OptionMenu = ('''
    Return Book Page:
    1. Return Book
    2. EXIT
'''
)

# List Menu in Visitor Homepage
homepage_VisitorMenu= ('''
        Visitor Homepage:
        1. View Book Availibilty
        2. Borrow Book
        3. Return Book
        4. "Mischief managed"
''')

# List Menu in System Administrator Homepage
homepage_AdminMenu = ('''
    System Administrator Homepage:
    1. View Book Availibilty
    2. Add New Book
    3. Edit Book Information 
    4. Delete Book
    5. Borrow Book
    6. Return Book
    7. "Mischief managed"
''')

# List Login Role
loginpage_OptionRole = ('''
    1. Login as System Admin (Librarian)
    2. Login as library visitor
    3. Exit
''')

# =========================================================================================================

from datetime import date

# Global variable
login_input=1



# ===========================================================================================================
# menu 1
# Provide option for user to view all and find specific book
def menu1():
        while True:
                print(viewOptionMenu)
                user_input_menu = int(input('Your entering View Page, please choose 1,2, or 3: '))
                print()
                if user_input_menu == 1:
                        menu1_showall()
                elif user_input_menu == 2:
                        menu1_find_id()
                elif user_input_menu == 3:
                    if login_input == 1:
                        homepage_admin()
                    elif login_input == 2:
                        hompage_visitor()
                else:
                    print('Please input available menu only, "1-3" ')
                    continue

# ===========================================================================================================
# Menu 1, sub 1: SHOW ALL BOOK
# User able to show all book that available in dictionary
def menu1_showall():
        print(f"ID \t Title \t\t Year \t Author \t Stock")
        for book in list_book:
                print(f"{book['ID']} \t \t {book['Title']} \t \t {book['Year']} \t \t {book['Author']} \t \t {book['Stock']}")

# =============================================================================================================
# Menu 1, sub 2: FIND BOOK BY BOOK ID
# User able to find specific book with book ID as parameter

# Function to find book by ID
def show_book_by_id(list_book, book_id):
    for book in list_book:
        if book['ID'] == book_id:
            print(f"ID \t Title \t\t Year \t Author \t Stock")
            print(f"{book['ID']} \t {book['Title']} \t {book['Year']} \t {book['Author']} \t {book['Stock']} \n")
            return True
    return False
# --------------------------------------------------

# Fuction to find specific book based on user input
def menu1_find_id():
    while True:
        input_keyid = (input('Please input Book ID: ')) # As example, if user input 002 , then system run process to find the 'ID'

        # Stored avalailble 'ID' from dictionary, later will be used for validation parameter
        list_id = []
        
        # This looping intended to get 'ID' value from dictionary stored to the list ID
        for book in list_book:
            list_id.append(book['ID'])
        
        # To validate if ID is valid or invalid, if valid then system will process to looping process
        if input_keyid in list_id:
           # If true, will go the next command to show book based on specific 'ID"
            for book in list_book:
                # Show specific book
                if book['ID'] == input_keyid:
                    show_book_by_id(list_book, input_keyid)
            break
        # if 'ID' can't be found (invalid), then system will give alert message and direct to  
        else:
            print('Book is not exist, please enter valid ID')
            menu1()


# ========================================================================================================================================
# Menu 2 
# Add Book page

def menu2():
    while True:
                print(addBook_OptionMenu)
                user_input_menu = (input('Your entering Add Book Page, please choose 1 or 2: ')) # As example if user input menu 1, system will direct user to sub menu borrow
                if user_input_menu == '1':
                    menu2_addbook()
                elif user_input_menu == '2':
                    break
                else:
                    print('Please input available menu only, "1-2" ')
                    continue

# =====================================================================================
# menu 2, sub 1 menu: Add book
# This menu allow user to add a new into a dictionary

def menu2_addbook():
    new_id = input('Enter Book ID: ')
    # Stored avalailble 'ID' from dictionary, later will be used for validation parameter
    list_id = []

    for book in list_book:
        list_id.append(book['ID'])

    if new_id in list_id:
        print('Book already exist, please input unique ID')
        menu2()
    else:
        Title = input('Input book title: ')
        Year = input('Input book year: ')
        Author = input('Input author name: ')
        Stock = int(input('Input book stock: '))
        newbook = {'ID':new_id,'Title':Title,'Year':Year,'Author':Author,'Stock':Stock}
        list_book.append(newbook)
        menu1_showall()



# ========================================================================================
# Menu 3
# Update Book

def menu3():
    while True:
                print(updateBook_OptionMenu)
                user_input_menu = int(input('Your entering Edit Book Page, please choose 1 or 2: '))
                print()
                if user_input_menu == 1:
                    print(f'\n{menu3_updatebook()}')
                elif user_input_menu == 2:
                    homepage_admin()
                else:
                    print('\nPlease input available menu only, "1-2" ')
                 


# ==============================================================================================
# menu 3, sub menu 1
# menu update book data information

def menu3_updatebook():
    while True:
        menu1_showall()
        input_bookid = input('\nEnter the book ID for the book you want to update: ')

        list_id = []

        for book in list_book:
            list_id.append(book['ID'])

        if input_bookid in list_id:
            for book in list_book:
                    # System will show specific books based on ID through a looping process
                    if show_book_by_id(list_book, input_bookid):

                        up_validation = input('Are you sure continue edit?(Yes/No): ')
                        if up_validation.lower() == 'no':
                            print('update has been cancel')
                            menu3()
                        elif up_validation.lower() == 'yes':
                            print(updateBook_DetailInformation)
                            choose_cat = input(f'Select the data category you want to update, (from 1 to 6):   ')
                            # find_index used to find index of dictionary based 'ID"
                            find_index = list_book.index(next(filter(lambda n: n.get('ID') == input_bookid, list_book)))
                            if choose_cat == '1':
                                show_book_by_id(list_book, input_bookid)
                                data_cat = (input('Enter New Book ID: '))
                                up_validation2 = input('Are you want keep the update?(Yes/No): ')
                                if up_validation2.lower() == 'yes':
                                    print('\n Data has been updated \n')
                                    list_book[find_index]['ID'] = data_cat
                                    show_book_by_id(list_book, data_cat)
                                    menu3()
                                elif up_validation2.lower() == 'no':
                                    print("Data failed to update")
                                    menu3()
                            elif choose_cat == '2':
                                show_book_by_id(list_book, input_bookid)
                                data_cat = (input('Enter change Title: '))
                                up_validation2 = input('Are you want keep the update?(Yes/No): ')
                                if up_validation2.lower() == 'yes':
                                    print('\n Data has been updated \n')
                                    list_book[find_index]['Title'] = data_cat
                                    show_book_by_id(list_book, input_bookid)
                                    menu3()
                                elif up_validation2.lower() == 'no':
                                    print("Data failed to update")
                                    menu3()
                            elif choose_cat == '3':
                                show_book_by_id(list_book, input_bookid)
                                data_cat = (input('Enter desire book Year: '))
                                up_validation2 = input('Are you want keep the update?(Yes/No): ')
                                if up_validation2.lower() == 'yes':
                                    print('\n Data has been updated \n')
                                    list_book[find_index]['Year'] = data_cat
                                    show_book_by_id(list_book, input_bookid)
                                    menu3()
                                elif up_validation2.lower() == 'no':
                                    print("Data failed to update")
                                    menu3()
                            elif choose_cat == '4':
                                show_book_by_id(list_book, input_bookid)
                                data_cat = (input('Enter desire book Author: '))
                                up_validation2 = input('Are you want keep the update?(Yes/No): ')
                                if up_validation2.lower() == 'yes':
                                    print('\n Data has been updated \n')
                                    list_book[find_index]['Author'] = data_cat
                                    show_book_by_id(list_book, input_bookid)
                                    menu3()
                                elif up_validation2.lower() == 'no':
                                    print("Data failed to update")
                                    menu3()
                            elif choose_cat == '5':
                                data_cat = (input('Enter desire book Stock: '))
                                up_validation2 = input('Are you want keep the update?(Yes/No): ')
                                if up_validation2.lower() == 'yes':
                                    show_book_by_id(list_book, input_bookid)
                                    print('\n Data has been updated \n')
                                    list_book[find_index]['Stock'] = data_cat
                                    show_book_by_id(list_book, input_bookid)
                                    menu3()
                                elif up_validation2.lower() == 'no':
                                    print("Data failed to update")
                                    menu3()
                            elif choose_cat == '6':
                                 menu3()
                            else:
                                print('\n Data category is not exist, please select 1-5!!!')
                                menu3_updatebook()
                        else:
                            print('Command can not be found, choose yes/n')
                            menu3()
        else:
            print('Data does not exist, please input valid book ID')
            menu3()
                

# ===========================================================================================
# menu 4
# Provid user for delete book feature
# Consist of delete and exit


def delete_book():
    while True:
        print(deleteBook_OptionMenu)
        user_input = int(input('Your entering Delete Book Page, please choose 1 or 2: '))

        list_id = []

        if user_input == 1:
            menu1_showall()
            del_book = input('Please choose book you want to delete, by enter book ID!: ')
            for book in list_book:
                list_id.append(book['ID'])

            if del_book in list_id:

                for item in list_book.copy():
                    if item.get('ID') == del_book:
                        fix_del = input('\n Are you sure want to delete?(Yes/No): ')
                        if fix_del.lower() == 'yes':
                            list_book.remove(item)
                            print('\n Data has been succesfully removed')
                            break
                        elif fix_del.lower() == 'no':
                            print('Data failed to delete!')
                            break
                print('\n')
                menu1_showall()
                break

            else:
                print('\n book is not exist, please input valid book ID')
                break

        elif user_input == 2:
            break
        else:
            continue
  
# =======================================================================================
# Menu 5
# This menu, allow user to borrow book
# Borrow book

def borrow_book():
    while True:
        print(borrowBook_OptionMenu)
        user_input = int(input('Your entering Borrow Book Page, please choose 1 or 2: '))

        if user_input == 1:
            sub_borrowbok()
        elif user_input == 2:
            if login_input == 1:
                homepage_admin()
            elif login_input == 2:
                hompage_visitor()
        else:
            print('wrong input, please try again!')
            borrow_book()

# =======================================================================================================
# Menu 5: sub 1
# Borrow book
# User allow to borrow book based on the availibility of stocks in dictionary

def sub_borrowbok():
    while True:
        menu1_showall()
        # find_index used to find index of dictionary based 'ID"
        borrow = input('Please enter the ID of the book you want to borrow!: ')
        find_index = list_book.index(next(filter(lambda n: n.get('ID') == borrow, list_book)))

        if list_book[find_index]['Stock'] != 0:
        # If book is available, then system wll continue checkout process
            borrow_confirmation = input('\n 1Are you sure want to borrow this book?(Yes/No): ')
            if borrow_confirmation.lower() == 'yes':
                book_stock = list_book[find_index]['Stock']-1
                list_book[find_index]['Stock'] = book_stock
                today = date.today()
                print(f'\n Happy reading, your book is successfully has been checkout at {today} \n')
            elif borrow_confirmation.lower() == 'no':
                borrow_book()
            else:
                print('\n You enter the wrong input, please choose Yes or No!\n')
                sub_borrowbok()
        elif list_book[find_index]['Stock'] == 0:
        # When book is unavailable (=0) then system wll give an alert message
            print('\n We are really sorry, the book you want to borrow is currently not available \n')
            menu1_showall()
        else:
            print('Wrong input, please enter correct book ID!')
    
        break


# ================================================================================================================
# Menu 6
# Return book
# This feature allow user to return book


def return_book():
    while True:
        print(returnBook_OptionMenu)
        user_input = int(input('Your entering Return Book Page, please choose 1 or 2: '))

        if user_input == 1:
            sub_returnbook()
        elif user_input == 2:
            if login_input == 1:
                homepage_admin()
            elif login_input == 2:
                hompage_visitor()
        else:
            print("You enter the wrong input, please try again!")
            return_book()

# ==============================================================================================================
# Menu 6
# Menu 6 : sub 1 = return book
# Return book feature allow user to return book, 
# and system will update the book stocks, once the book has been return

def sub_returnbook():
    while True:
        menu1_showall()

        # find_index used to find index of dictionary based 'ID"
        borrow = input('Please enter the ID of the book you want to return!: ')
        find_index = list_book.index(next(filter(lambda n: n.get('ID') == borrow, list_book)))

        # Stored avalailble 'ID' from dictionary, later will be used for validation parameter
        list_id = []

        # To validate if ID is valid or invalid, if valid then system will process to looping process
        for book in list_book:
            list_id.append(book['ID'])

        if borrow in list_id:
            borrow_confirmation = input('Do you want to return this book?(Yes/No): ')
            if borrow_confirmation.lower() == 'yes':
                book_stock = list_book[find_index]['Stock']+1
                list_book[find_index]['Stock'] = book_stock
                today = date.today()
                print(f'\n Thank you, your book is successfully has been return at {today} \n')
                print('Looking forward for the next book')
            elif borrow_confirmation.lower() == 'no':
                menu1_showall()
        else:
            print('Wrong input, please enter correct book ID!')
            return_book()

        break

# ===========================================================================================================================
# Homepage 2 consist of main menu, intended for user that has role as library vistor's


def hompage_visitor():
        while True:
                print(f'''
                Welcome to Duke Humfrey's Library
                "I solemnly swear that I am up to no good"

                Find your inspiring literature, by start entering here\n
                ''')

                print(homepage_VisitorMenu)
                # System will direct user to choose menu on homepage_visitor
                user_input_menu = int(input("Your entering Duke Humfrey's Visitor Homepage, please choose 1,2,3, or 4: "))
                print()
                # If input true, then system will direct to the menu that user has been chose
                # if input is false, then system will show alert message and direct to homepage_visitor again
                if user_input_menu == 1:
                    menu1()
                elif user_input_menu == 2:
                    borrow_book()
                elif user_input_menu == 3:
                    return_book()
                elif user_input_menu == 4:
                    print('Looking forward your next reading, keep motivated :) \n')
                    login_page()
                else:
                    print('Menu is not exist, please input the correct number')

# =================================================================================================================
# Homepage 1 consist of main menu, intended for user that has role as System Admin (librarian)
# System Admin will get full access of featues that is available in Duke Humfreys Library

def homepage_admin():
        while True:
            print(f'''
            Welcome to Duke Humfrey's Library
            "I solemnly swear that I am up to no good"
            ''')
            
            print(homepage_AdminMenu)
            # System will direct user to choose menu on homepage_visitor

            user_input_menu = int(input("Your entering Duke Humfrey's System Administrator Homepage, please choose 1,2,3,,4,5,6 or 7: "))
            print()
            # If input true, then system will direct to the menu that user has been chose
            # if input is false, then system will show alert message and direct to homepage_admin again
            if user_input_menu == 1:
                menu1()
            elif user_input_menu == 2:
                menu2()
            elif user_input_menu == 3:
                menu3()
            elif user_input_menu == 4:
                delete_book()
            elif user_input_menu == 5:
                borrow_book()
            elif user_input_menu == 6:
                return_book()
            elif user_input_menu == 7:
                print('Looking forward your next reading, keep motivated :) \n')
                login_page()
            else:
                print('Menu is not exist, please input the correct number')

# ================================================================================================================
# Login page
# This application will give different authority of access based on role that user choose


def login_page():
        while True:
            print(f'''
            "Your about entering to a Duke Humfrey's Library, 
            a start for your a whole new world!"
            ''')
            print(loginpage_OptionRole)

            # The system will ask for user input to login according to the type of user available
            user_input_login = int(input('\n Choose login as.. '))

            global login_input
            login_input = user_input_login

            # If input true, then system will direct to the appliaction as a role that has been chose
            # if input is false, then system will show alert message and login page again
            if user_input_login == 1:
                homepage_admin()
            elif user_input_login == 2:
                hompage_visitor()
            elif user_input_login == 3:
                print('Adios, catch you around pal! \n')
                exit()
            else:
                print('Menu is not exist, please input the correct number')
login_page()

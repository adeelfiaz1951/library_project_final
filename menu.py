from model import LibraryCatalog, Book, Member

def start_menu():
    catalog = LibraryCatalog()

    while True:
        '''
        print("\n===== Library Menu =====")
        print("1. View all books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Register a member")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. Exit")
        '''
        choice = input("Enter choice: ")

        # view books

        if choice == '1':
            print('\n---All Books---')
            if len(catalog.books) == 0:
                print('No books available')
            else:
                for b in catalog.books:
                    print(f'ID: {b.book_id} | Title: {b.title} | Author: {b.author}')

        # 2 Add books
        elif choice == '2':
            print('\n---Add Book---')
            try:
                book_id = int(input('Enter book ID: '))
            except:
                print('Invalid ID')
                continue

            title = input('Title: ')
            author = input('Author: ')
            year = input('Year: ')
            genre = input('Genre: ')
            
            book = Book(book_id, title, author, year, genre)
            catalog.add_book(book)
            print('Book added succefully.')

        # Remove book
        elif choice == '3':
            print('\n---Remove book---')
            try:
                book_id = int(input("Enter book id to remove a book: "))
            except:
                print('Invalid ID')
                continue

        # Register member
        elif choice == '4':
            print('\n---Register Member---')
            try:
                member_id = int(input('Enter member id: '))
            except:
                print('Invalid ID')
                continue

            name = input('Name: ')
            email = input('Email: ')

            member = Member(member_id, name, email)
            catalog.register_member(member)
            print('Member Registered!')

        # Borrow book
        elif choice == '5':
            print('\n---bORROW book---')

            try:
                member_id = int(input('Member ID: '))
                book_id + int(input('Book ID'))
            except:
                print('invalid input')
                continue
                
        elif choice == "6":
            print("\n--- Return Book ---")
            try:
                member_id = int(input("Member ID: "))
                book_id = int(input("Book ID: "))
            except:
                print("Invalid input")
                continue

            if catalog.return_book(member_id, book_id):
                print("Book returned successfully!")
            else:
                print("Return failed! Member or Book may not exist.")

        # -------------------------------------------------
        # 7. EXIT
        # -------------------------------------------------
        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


        
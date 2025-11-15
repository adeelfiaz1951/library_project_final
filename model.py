import json

# simple book class
class Book:
    def __init__(self, book_id, title, author, year, genre):
        self.book_id = book_id,
        self.title = title,
        self.author = author,
        self.year = year,
        self.genre = genre
    
    # convert book to a dictionary for JSON
    def  to_dict(self):
        return {
            'book_id' : self.book_id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre
        }
    
class Member:
    # simple member class

    def __init__(self, member_id, name, email):
        self.member_id = member_id,
        self.name = name,
        self.email = email
        self.borrowed_books = []

    def borrow(self, book_id):
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
    
    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)

    def to_dict(self):
        return{
            'member_id' : self.member_id,
            'name' : self.name,
            'email': self.email,
            'borrowed_books' : self.borrowed_books
        }
      
    # Handle books, members, borrowing, JSON savings 
class LibraryCatalog:

    def __init__(self, file_path ='catalog.json'):
        self.file_path = file_path,
        self.books = [],
        self.members = [],
        self.load_data()

    # Json handling
    def load_data(self):
        # Load data from json create file if missing
        try:
            with open(self.file_path, 'r') as f:
                data =  json.load(f)

            # Load books

            for b in data.get('books', []):
                self.books.append(Book(b['book_id'], b['title'], b['author'], b['year'], b['genre']
                ))
            
            # Load members

            for m in data.get('members', []):
                member = Member(m['member_id'], m['name'], m['email'])
                member.borrowed_books = m.get('borrowed_books', [])
                self.members.append(member)
        except FileNotFoundError:
            self.save_data()  # create a new file if missing

    def save_data(self):
        #'Save all data to json'
        data ={
            'books': [b.to_dict() for b in self.books],
            'members': [m.to_dict() for m in self.members]
        }

        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    # Book management

    def add_book(self, book):
        self.books.append(book)
        self.save_data()
    def remove_book(self, book_id):
        self.books = [b for b in self.books if b.book_id != book_id]
        self.save_data()
    def find_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                return b
        return None
    
    # member management

    def register_member(self,member):
        self.members.append(member)
        self.save_data()

    def find_member(self, member_id):
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None
    
    # Borrowing sysytem

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member and book:
            member.borrow(book_id)
            self.save_data()
            return True
        return False
    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)

        if member:
            member.return_book(book_id)
            self.save_data()
            return True
        return False





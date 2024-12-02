class Library:

    books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 4},
    {"id": 2, "title": "1984", "author": "George Orwell", "copies": 5},
    {"id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "copies": 3},
    {"id": 4, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 2},
    {"id": 5, "title": "Moby Dick", "author": "Herman Melville", "copies": 1}
    ]

    members = [
    {"name": "jonh", "roll_no":"0001", "membership_status":"Active", "books_issued":["To Kill a Mockingbird"]},
    {"name": "emily", "roll_no":"0002", "membership_status":"Inactive", "books_issued":["1984", "Pride and Prejudice"]},
    {"name": "michael", "roll_no":"0003", "membership_status":"Active", "books_issued":["The Great Gatsby"]},
    {"name": "sophia", "roll_no":"0004", "membership_status":"Active", "books_issued":["Moby Dick", "The Odyssey"]}
    ]

    
    def __init__(self):
        pass
#--------------------------------------Books in library------------------------------------------
    # Show Books Method
    @classmethod    
    def show_books(cls):
        
        for book in cls.books:

            print(f"{book['id']}. {book['title']} by {book['author']}, No of copies: {book['copies']}")

    # This method will store new books info
    def add_new_book_info(self):
        title = input('Insert book title')
        author = input('Insert Authors name')
        copies = input('Insert no# of copies')
    
        book = Book(title, author, copies)#we are passing the input info to book class
        book.add_new_book()# we have called this function over here because it is not being called down below

    #This method will take in the info of the book that we want to remove    
    @classmethod
    def remove_book_info(cls):
        remove_this = int(input('Insert book ID to remove the book: '))
        Book.remove_book(remove_this)
           
#--------------------------------------Members in library------------------------------------------
    @classmethod
    def show_members(cls):
        for member in cls.members:
            print(f"Name: {member['name']}")
            print(f"Roll-no: {member['roll_no']}")
            print(f"Membership-status: {member['membership_status']}")
            print(f"Books-issued: {member['books_issued']}")
            print("----------------------------------------------")

    #This method will add new members info
    def add_new_member_info(self):
        name = input("Enter Name")
        roll_no = input("Enter Roll-no")

        member = Member(name, roll_no)

        member.add_new_member()
    #This method will remove the member
    @classmethod
    def remove_member_info(cls):
        remove_this = int(input('Insert members roll-no to remove the book: '))
        Member.remove_member(remove_this)

#--------------------------------------Book Class------------------------------------------
class Book(Library):

    def __init__ (self, title, author, copies):
        
        self.title = title
        self.author = author
        self.copies = copies

    #This method will add new book to the list
    def add_new_book(self):
        new_id = len(Library.books) + 1
        new_book = {
            "id": new_id, 
            "title": self.title, 
            "author": self.author, 
            "copies": self.copies
        }
    
        Library.books.append(new_book)

    #This method will remove the book
    @classmethod
    def remove_book(cls, remove_this):

        for book in cls.books:
            if book["id"] == remove_this:
                cls.books.remove(book)
                break

    #This part will adjust the index...            
        for index, book in enumerate(cls.books): 
            book["id"] = index + 1             

#--------------------------------------Member Class------------------------------------------
class Member(Library):

    def __init__(self, name, roll_no):
        super(Library).__init__(self)

        self.name = name
        self.roll_no = roll_no
        self.membership_status = "Active"
        self.books_issued = []

    def add_new_member(self):

        new_member ={
            "name" : self.name,
            "roll_no" : self.roll_no,
            "membership_status" : "Active",
            "books_issued" : []
        }

        Library.members.append(new_member)
        print(f"Member {self.name} added successfully.")

    #This method will remove the book
    @classmethod
    def remove_member(cls, remove_this):

        for member in cls.members:
            if member["roll_no"] == remove_this:
                cls.books.remove(member)
                break



#-------------------------------------------------------------------------------------------
#Instances
library = Library()


while True:
    print("1. Manage Books")
    print("2. Manage Members")
    print("3. Exit")

    choice = input("Enter your choice")

    if choice == '1':

        while True:
            print("\n1. Show books")
            print("2. Add a new book")
            print("3. Remove a book")
            print("4. Exit")
    
            choice = input("Enter your choice: ")

            if choice == '1':
                library.show_books()
            elif choice == '2':
                library.add_new_book_info()
            elif choice == '3':
                library.remove_book_info()
            elif choice == '4':
                break
            else:
                print("Invalid choice, please select again.")
    
    elif choice == '2':
        while True:
            print("\n1. Show Members")
            print("2. Add a new Member")
            print("3. Remove a book")
            print("4. Exit")
    
            choice = input("Enter your choice: ")

            if choice == '1':
                library.show_members()
            elif choice == '2':
                library.add_new_member_info()
            elif choice == '3':
                library.remove_member_info()
            elif choice == '4':
                break
            else:
                print("Invalid choice, please select again.")

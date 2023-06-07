# Define a class “Book” to store the details author, book name, price, status, rack number and edition.
# Create display book function to display the details of the book and an update function to update the
# details of book. Create a class called “Librarian” having members name and password. Define a
# function search book, return book and issue book.

class Book :
    book_lst=dict()
    def __int__(self) :
        self.author=''
        self.bookname=''
        self.price=''
        self.status=-1
        self.racknumber=-1
        self.edition=-1
    
    def update(self) :
        self.bookname=input('Enter the Book name :')
        if self.bookname not in self.book_lst :
            self.book_lst[self.bookname]=0
        self.author=input('Enter the author :')
        self.price=int(input('Enter the price :'))
        self.racknumber=int(input('Enter the rack number :'))
        self.edition=int(input('Enter the edition :'))

    def display(self) :
        print('Book name :',self.bookname)
        print('Author :',self.author)
        print('Price :',self.price)
        print('Rack number :',self.racknumber)
        print('Edition :',self.edition)
    
class Librarian(Book) :
    def __init__(self) :
        super().__init__()
        self.users={'Carl':['1234',''],'Joe':['789',''],'Ram':['345','']}
        
    def check(self,user,pas) :
        if user in self.users.keys() :
            if pas==self.users[user][0] :
                return True
            else :
                return False
        else :
            return False
    
    def searchbook(self) :
        search=input('Enter the book name :')
        if search in self.book_lst :
            print('Book Found')
        else :
            print('Book not Found')
    
    def issue(self) :
        user=input('Enter the user name :')
        pas=(input('Enter the password :'))
        if self.check(user,pas) :
            book=input('Enter the book name :')
            self.users[user][1]=book
            self.book_lst[book]=1
            print('Book issued successfully!')
        else :
            print('Username or password is incorrect ')     
    
    def book_return(self) :
        book=input('Enter the book name :')
        if self.book_lst[book]==1 :
            user=input('Enter the user name :')
            if user in self.users.keys() :
                self.book_lst[book]=0
                self.users[book][1]=''
                print('Book returned successfully!')
            else :
                print('Username not present')
        else :
            print("Book already returned or Book not Found")
    
book1=Book()
if input('Do you want to update the book details :')=='Yes' :
    book1.update()
if input('Do you want to display the book details :')=='Yes' :
    book1.display()

person1=Librarian()
if input('Do you want to search book :')=='Yes' :
    person1.searchbook()
if input('Do you want to issue a book :')=='Yes' :
    person1.issue()
elif input('Do you want to return a book :')=='Yes' :
    person1.book_return()

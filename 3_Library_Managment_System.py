class Library :
    def __init__(self,listOfBooks):
        self.books = listOfBooks
        
    def displayAvailableBooks(self) :
        print("Books Present in Library are : ")
        for book in self.books :
            print(" *" + book)
            
    def borrowBook(self,bookName) :
        if bookName in self.books :
            print(f"{bookName} book has been Issued.Please Keep it Safe and Handle it properly")
            self.books.remove(bookName)
            return True
        else :
            print("This book has been issued by someone else. Kindly wait till he returns the book to us.")
            return False
    
    def returnBook(self,bookName) :
        self.books.append(bookName)
        print("Thanks! for returning the book.")
         
         
class Student : 
    def requestBook(self) :
        self.book = input(f"Enter a book name, You requested : ")
        return self.book
    
    def returnBook(self) :
        self.book = input(f"Enter a book name, You want to Return : ")
        return self.book

if __name__ == "__main__" : 
    centralLibrary = Library(["DSA","Robust Python","Web Development","Machine Learning"])
    studentObj = Student()

    while(True) :
        welcomeMsg = ''' Welcome to the Central Library
        Choose following to Implement
        1. Display Available Books
        2. Request Book
        3. Add/Return Book
        4. Exit From Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a Choice : ")) 
        
        if a==1 :
            centralLibrary.displayAvailableBooks()
        
        elif a==2 :
            centralLibrary.borrowBook(studentObj.requestBook())
   
        elif a==3 :
            centralLibrary.returnBook(studentObj.returnBook())
            
        elif a==4 :
            print("Thanks! For using our Library Management System")
            exit()
            
        else  : 
            print('Invalid Option ')
            
        

        
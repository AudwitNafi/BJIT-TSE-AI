class User:
    ##storing user count to generate unique id each time a user created
    userCount = 0
    def __init__(self, name, bookList):
        self._name = name ##protected attribute
        self._id = self.createId() ##protected attribute
        self._bookList = bookList ##protected attribute
        print(f"User created. Name: {self._name}, ID: {self._id}")
    
    @classmethod
    def createId(cls):
    ##a unique id is created by incrementing the userCount class variable
        cls.userCount += 1
        return cls.userCount
    
    def getName(self):
        return self._name
    
    def getId(self):
        return self._id
    
    def borrow(self, bookTitle):
        pass
    
    def returnBook(self, bookTitle):
        if len(self._bookList)==0:
            print("No books to return!")
            return
        if len(bookTitle)==0:
            print("Please Provide a Book Title")
        elif (bookTitle not in self._bookList):
            print("This book has not been borrowed by the user.")
        else:
            self._bookList.remove(bookTitle)
            print(f"{self._name} returned '{bookTitle}'")
    
    def booksBorrowed(self):
        return self._bookList
    
    def numberBorrowed(self):
        return len(self._bookList)
    

class Student(User):
    def __init__(self, name, bookList):
        User.__init__(self, name, bookList)
        self._id = User.createId()
        self.borrowLimit = 3
         
    def borrowBook(self, bookTitle):
        if(len(self._bookList)>=self.borrowLimit):
            print("You are at your borrow limit!")
            return
        if len(bookTitle)==0:
            print("Please Provide a Book Title")
        else:
            self._bookList.append(bookTitle)
            print(f"{self._name} borrowed '{bookTitle}'")

class Professor(User):
    def __init__(self, name, bookList):
        User.__init__(self, name, bookList)
        self._id = User.createId()
        self.borrowLimit = 5 
        
    def borrowBook(self, bookTitle):
        if(len(self._bookList)>=self.borrowLimit):
            print("You are at your borrow limit!")
            return
        if len(bookTitle)==0:
            print("Please Provide a Book Title")
        else:
            self._bookList.append(bookTitle)
            print(f"{self._name} borrowed '{bookTitle}'")
            
s1 = Student("Nafi", [])
p1 = Professor("Sarwar San", [])

s1.borrowBook("Jane Austen - Pride & Prejudice")
s1.borrowBook("Harry Potter and The Deathly Hallows Pt.1")
s1.borrowBook("Harry Potter and The Order of The Phoenix")
s1.borrowBook("Limit Testing")
s1.returnBook("")
s1.returnBook("Testing Not Borrowed Book")
s1.returnBook("Jane Austen - Pride & Prejudice")

print(f"{s1.getName()}, id {s1.getId()}, has borrowed the following {s1.numberBorrowed()} books:", s1.booksBorrowed())

p1.borrowBook("Newtonian Mechanics")
p1.borrowBook("Java How to Program")
p1.borrowBook("System Design Fundamentals")
p1.borrowBook("Object Oriented Programming in C++")
p1.borrowBook("Professional's Guide to AI Engineering")
p1.borrowBook("Limit Testing")

p1.returnBook("ABC")
p1.returnBook("Newtonian Mechanics")

print(f"{p1.getName()}, id {p1.getId()}, has borrowed the following {p1.numberBorrowed()} books:", p1.booksBorrowed())
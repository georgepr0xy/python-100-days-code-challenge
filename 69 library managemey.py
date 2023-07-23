class library():
    def __init__(self):
        self.nobooks=0
        self.books=[]

    def addbooks(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)

    def showinfo(self):
        print(f"the no. of books is {self.nobooks}, the books are : \n")
        for i in self.books:
            print(i)   


l1 = library()
l1.addbooks("The Bhagwatgeeta")
l1.addbooks("Ramayana")
l1.addbooks("Mahabharat")
l1.addbooks("The money")
l1.addbooks("Marvelcomics")
l1.showinfo()
                 
        

class Book:
    def __init__(self,title,author,year):

        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def show_info(self):
        if self. available == True:
            print(f'Available! The Book Is {self.title} The Author Is {self.author}')
        else :
            print("Not Found")

    def borrow(self):
        if self.available == True:
            
            self.available = False
            print(f"You Have Borrowed {self.title}")
        else:
            print("not available")

    def return_book(self):

        self.available = True
        print(f'{self.title} is now available')


b1 = Book("python","elmohande academy",2022)
b1.borrow()
b1.borrow()

b1.return_book()
b1.borrow()
class Fiction (Book):
    def __init__(self, title, author, year, gener):
        super().__init__(title, author, year)
        self.gener = gener
class Science (Book):
    def __init__(self, title, author, year,field):
        super().__init__(title, author, year)
        self.field = field
        def show_info(self):
            print (f'The Book Gener Is (self.gener)')
f1 = Fiction("python for kids ",'fatma',2024,'programming')
f1.show_info()
f1 = Fiction("python for kids ",'fatma',2024,'math')
f1.show_info()








              
            

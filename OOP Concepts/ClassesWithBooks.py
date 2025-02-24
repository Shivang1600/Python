#Create a class called Book with attributes like title, author, and publication_year. Create several instances of the Book class and print their details.

class Book:
    def __init__(self, title, author, publication_year):
     self.title = title
     self.author = author
     self.publication_year = publication_year
 
    def display_book_details(self):
       print("\n"f"\nTitle: {self.title}, \nAuthor: {self.author}, \nPublication Year: {self.publication_year}")


book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("Pride and Prejudice", "Jane Austen", 1813)

book1.display_book_details()
book2.display_book_details()
book3.display_book_details()




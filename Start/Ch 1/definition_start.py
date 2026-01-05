# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book: # can add () but only if it inhereits from another class
  def __init__(self, title): #called to initialize before any other function
    self.title = title #creating a new attribute called title that contains the variables from book
  
  #pass # will do nothing but you can now create instances from it

# TODO: create instances of the class
book1 = Book("Brave New World")
book2 = Book("War and Peace")

# TODO: print the class and property
print(book1)
print(book1.title)
#Create a function that adds a book to a reading list then displays the list
def readingList(books):
    print("Here are some books I will read:")
    numofBooks = 0
    for book in books:
        print(book)
        numofBooks = numofBooks + 1
        print(numofBooks, 'total books to read')

#--------------------------------------------------------------------
def readingList(books):
    print("Here are some books I will read:") #1 step
    numofBooks = 0                            #1 step
    for book in books:                        #n * steps in the loop
        print(book)                           #1 step
        numofBooks = numofBooks + 1           #1 step
        print(numofBooks, 'total books to read') #1 step
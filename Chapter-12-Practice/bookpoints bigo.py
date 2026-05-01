#Creates a function to count points per book read
def countBookPoints(books):
    points = 0                  # 1 step
    for book in books:          # n * steps in the loop
        points += 1             #1 step

#If the book is by Al Sweigart then another point is gained
    for book in books:          #n * steps in the loop
        if 'by Al Sweigart' in book:    # 1 step
            points += 1                 # 1 step

    return points                       #1 step

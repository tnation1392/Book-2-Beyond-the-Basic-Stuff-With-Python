#Creates a function to calculate the perimeter of a rectangle
def rectanglePerimeter(rect):
    return (rect[0] * 2) + (rect[1] * 2)

myRectangle = [4,10]

print(rectanglePerimeter(myRectangle))
#-------------------------------------------------------------
# Now we create a lambda function for this
rectanglePerimeter = lambda rect: (rect[0] * 2) + (rect[1] * 2)

print(rectanglePerimeter([4,10]))
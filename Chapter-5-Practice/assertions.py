#Creates a function that calculates the average of a list of numbers.
#Adds assertions to make sure the list isn't empty and all items are numeric

def average(numbers):
    total = sum(numbers)

    assert len(numbers) > 0, "List must not be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), \
        "All items in the list must be numbers (int or float)"

    return sum(numbers) / len(numbers)






average([10, 20, 30])    #Works
average([10, 2.5, 3])    #Works
average([10, "20", 30])  #AssertionError
average([])              #AssertionError

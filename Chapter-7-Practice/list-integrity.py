#The function listed returns an average from a list of numbers

def average(numbers):
    total = sum(numbers)

    #Create assertions that make sure the list is not empty, and that it has numerical values
    assert len(numbers) > 0, "List must not be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), \
        "All items in the list must be numbers (int or float)"

    return sum(numbers) / len(numbers)

average([1, 2, 3])
average([])
average([1, "two", 3])

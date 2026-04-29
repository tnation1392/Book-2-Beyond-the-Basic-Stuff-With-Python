#Creates a function that returns a list
def handle_list(items):
    return [i for i in items if i % 2 == 0]

#The name of the function does not tell what it does
#-------------------------------------------------------

def return_even(items):
    return [i for i in items if i % 2 == 0]

print(return_even([1,2,3,4,5,6]))
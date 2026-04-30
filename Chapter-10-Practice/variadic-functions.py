#Creates a function that multiplies any given numbers together
def product(*args):
    result = 1
    for x in args:
        result *= x
    return result

print(product(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#-----------------------------------------------------------------

#Creates a function to find the minimum value in a set of values
def myMinfunction(*args):
    if len(args) == 1:
        values = args[0]
    else:
        values = args

#Raise an error if no values are present
    if len(values) == 0:
        raise ValueError('myMinFunction() args is an empty list')

#Loops through the sequence until the smallest value is found
    for i, value in enumerate(values):
        if i == 0 or value < smallestValue:
            smallestValue = value
    return smallestValue

#------------------------------------------------------------------
#Creates a function with kwargs as many keyword molecules
def formMolecules(**kwargs):
    if len(kwargs) == 1 and kwargs.get('unobtanium') == 12:
        return 'Aether'

print(formMolecules(unobtanium=12))
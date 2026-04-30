#Creates a function that prints out names in lower case
def printLower(*args, **kwargs):
    args = list(args)
    for i, value in enumerate(args):
        args[i] = str(value).lower()
    return print(*args, **kwargs)

#name is the keyword to be used
name = "Todd"

#Use "Hello" as the arg and name as the kwarg
print(printLower('Hello', name))
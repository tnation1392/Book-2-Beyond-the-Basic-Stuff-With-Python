#refactor the whole function
def d(s, n):
    r = ""
    for i in range(n):
        r += s
    return r
#-------------------------------------------
#Test the function to show results for context
print(d("cat", 5))

#Function concatenates a list based on a given string and number of times to do so
def concat_string(string, number):
    r = ""
    for i in range(number):
        r += string
    return r

print(concat_string("cat", 5))
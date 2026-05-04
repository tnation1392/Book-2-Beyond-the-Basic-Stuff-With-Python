class Classwithregattributes:
    def __init__(self, someParameter):
        self.someAttribute = someParameter

obj = Classwithregattributes('some initial value')
print(obj.someAttribute)  # Prints 'some initial value'
obj.someAttribute = 'changed value'
print(obj.someAttribute)  # prints changed value
del obj.someAttribute  # Deletes the someAttribute attribute

#-------------------------------------------------------------------------

def ClasswithProperties():
    def __init__(self):
        self.someAttribute = 'some initial value'

    @property
    def someAttribute(self): #The getter method
        return self.someAttribute

    @someAttribute.setter
    def someAttribute(self, value): #The setter method
        self.someAttribute = value

    @someAttribute.deleter
    def someAttribute(self): #The deleter method
        del self.someAttribute

obj = ClasswithProperties()
print(obj.someAttribute) #Prints 'some initial value'
obj.someAttribute = 'changed value'
print(obj.someAttribute) #prints 'changed value
del obj.someAttribute #deletes the attribute
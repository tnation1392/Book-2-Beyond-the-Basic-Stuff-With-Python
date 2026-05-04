class ExampleClass:
    def exRegularMethod(self):
        print("This is a regular method")

    @classmethod
    def exclassMethod(self):
        print("This is a class method")

#Call the class Method
ExampleClass.exclassMethod()

obj = ExampleClass()
#Regular Method
obj.exRegularMethod()
#Class Method
obj.__class__.exclassMethod()
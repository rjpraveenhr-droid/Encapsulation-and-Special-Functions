# Class creation
class myClass:

    # private variable
    __privateVar = 27;

    # private method
    def __privMeth(self):
        print("I'm inside my class myClass")

    # function to print value 
    def hello(self):
        print("Private Variable value: ",myClass.__privateVar)

# Object creation and method
foo = myClass()
foo.hello()
foo.__privMeth
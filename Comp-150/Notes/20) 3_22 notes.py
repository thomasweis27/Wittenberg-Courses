#Class - a object that cna hold veriables and functions
#       When we create an object from a class it is an 'instance'

#what should a car have? (atributes)
#what should an object be able to do? (functions)



#self.var = something
#def otherFunction(self, other perameters):
    #stuff here

class Person:    #classes are usually has uppsecase first letter

    #the constructor
    def __init__(self, name, dob, height):
        self.name = name
        self.dob = dob
        self.height = height
        #self means it is a veriable of the class + object and
        #   are therefor a different veriable ("instance veriable")


    #getter function
    def getName(self):
        return self.name


    #setter function
    def setHeight(self, newHeight):
        self.height = newHeight



    

def main():
    p1 = Person("John", "11/22/1900", 64)
    print (p1.name)   #not the right way

    print(p1.getName()) #good way (called a getter)

main()

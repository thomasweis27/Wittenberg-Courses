#Veriables continued
#   additionally a veriable name can not start with a digit
#   veriables (and everything in python) is case sensitive
#   no dashes and no spaces in verable name

space_var = 3 #dont add a space where the underscore is

name = "Thomas"
nAmE = "Weis"
print (name, nAmE)

# names should be discriptive (like 'area' or 'radiusOfSphere')   
#   mixed case is the name for something like 'radiusOfSphere'
#       stay consistant with naming styles


#more asignments
x = y = 3
print (x)
print (y)

x, y = 5, 7
print (x)
print (y)

x, y = y, x
print (x)
print (y)


#inputVeriable = input("Message asking for something for the user to input: ")

userName = input("Enter yout name: ")
print("Hello", userName)
type(userName)

#no matter the input, it will be treated as a string

userAge = eval(input("Enter your age: "))    #do not use! Points will be taken off for use!! (will run code the user enters)
userAge = int(input("Enter your age: "))
userAge = float(input("Enter your age: "))

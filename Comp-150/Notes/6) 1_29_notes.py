# Comenting - adding text to clde that explains the purpose and workings of code
#     It is to help people and us reading it in the future.

# Where to add comments
#   ~beginning of file explaining purpose of lab
#   ~at the beginning of exery function showing imut needed, output, and what it does
#   ~lines of code that are not super easy to look at and understand

"""this is also a
    comment technally
    and is many lines.
    don't use this
    though usually"""

#More examples of floats
x = 3e6    #means 3*10^6
r = -0.0
print(x, r)

#use strings mostly for testing
# can use double or single quotes

str1="this is a string"
str2= 'this is also a string'
str3= '"this is also a string"'
##    ""this is not a string""
print(str1)
print(str2)
print(str3)
print()

#Checking the type of the veriable
print(type(x))
print (type(str1))

f4 = float(4)
print(4)
print (f4)
print(type(4.0))

#can change str to float but only if it is a single number
x=int(55.0)
print(x)

s = "Hello"+" World " +str(x)    #This all needs to be a string
print(s)

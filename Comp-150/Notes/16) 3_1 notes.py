#escape characters
#  \n (new line)
#  \t (tab)
#  \' (print single quote)
#  \" (print double quote)
#  \\ (singular backslash)
#  \b (backspace)

print ("Hello", end=" ")
print ("world")
print ("Hello\nWorld")
print ("\\")
print ("\"Hello World\"")

#String Formatting
# stringVar.format(value1, value2, ...)
# first set of {} goes to first value
# the num of {} must match number of values
#

userName = input("What is your name? ")
print ("Hello {}!".format(userName))

# {:.2f} formats to two desimal places
# {:d} formats as a decimal (number in base ten)
# {:0>4d} formats desimal to take up more than 4 spaces (pad with 0s)
# {:b} formats as binary number
# {:4s} format string to take at least 4 characters
# {:>8s} format string to be right justified and take 8 spaces
# {:<10s} format string to be left justified and take 10 spaces

print ("Hello{:>8s}".format("test")) #test included in the 8 spaces
print ("{:0>8s}".format("3"), "!")
print ("{:0<8s}".format("3"), "!") # left justified number makes 0's after the 3

string = "Hello World"
endswith = string.endswith("d") #check to see if string ends with given thing
print(endswith)

for c in string:
    print(c, end=",") #seporates all parts of a string with comma
print(), print()

for c in string:
    if string.endswith(c): #removes comma at the end
        print(c)
    else:
        print(c, end=",")

str1 = "qwertyuiop" #can print part of a string
c = str1[3]
print (c)
print (str1[:4]) #before 4
print (str1[0: :2]) # after skipping every other number
print("The length of the string is", len(str1))

str3 = "Hello World\b" #"\b"is one character so looks like 10
print(len(str3))
print(str3)




# check if number of between 0 and 10 or between 100 and 200

num = int(input("Please enter a number: "))

if (num >= 0 and num <= 10) or (num >= 100 and num <= 200):
    print ("good number")
else:
    print ("Bad number")


#order logical oporations
#not
#and 
#or
#does it in this order beginning with not first


#Short Circuiting
#When there is a logical oporator and the first argument if false,
#  we do not compute the second argument

# a and b   <- if a is false we do not compute b
# a or b    <- if a is true  we do not compute b

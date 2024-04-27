#function - a piece of code to repeat
#
#usually has inputs and outputs but doesn't need to
#basically, use a function if you are writing the same code over and over


#def functionName (peramater):    (veriables going to be used in function)
#   code here
#   can be many lines
#
#   optional
#   return value

def fun(x):
    result = x**2 + 1   #function result
    return result

#find z squared + 1
z=4
result = fun(z)         #different result, diffrent places, different veriables
print (z, result)


#name doesn't matter being passed in (z becomes x in function),  
#   its not the name that matters but the order put in
#       Ex. (y, z) in function can be (a, b)or (y, z) THEY ARE DIFFERENT VERIABLES
#           numbers can even be reused

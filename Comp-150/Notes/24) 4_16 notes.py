#  s=c0c1c2c3c4...cN

#Take the fizt char off, reverse the rest of the string, put the first
#      char back at the end.

# Bass case = if the length of the string is 0 or 1



def reverseString(s):
    if s == "":
        return s



    firstChar = s[0]
    restOfString = s[1:]
    rev = reverseString(restOfString)
    finStr = rev + firstChar

    return finStr




s = "123456789"
re = reverseString(s)
print (re)

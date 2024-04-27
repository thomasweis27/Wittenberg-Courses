#  s=c0c1c2c3c4...cN

#make the string have size each time

# Bass case = if the length of the string is 0 or 1



def reverseString(string):
    if len(string)<= 1:
        return string

    length = len(string)
    half = string[:(length//2)]
    second = string[(length//2):]
    firsthalf = reverseString(half)
    secondhalf = reverseString(second)

    reversedString = secondhalf + firsthalf
    
    return reversedString




s = "abcdefghijklmnopqrstuvwxyz"
re = reverseString(s)
print (re)

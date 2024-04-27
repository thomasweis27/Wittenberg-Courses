# else is not needed for a condition
#
# if condition:
#   consequent
#else:
#   pass


print ("absolute value")
num = 12
if num < 0:
    num = -1*num
#else:
#    pass
print (num)


#another if statement can be used as a condition/consequent


#if conditionOne:
#elif conditionTwo:
#elif conditionThree:
#else all above false


#Boolian expressions use three logic oporators:
#   and (a and b)
#   or (a or b)
#   not (not a)


userNum = int(input("What is the number? "))
             
if userNum >= 0 and userNum <= 10:
    print("The number is between 0 and 10.")
else:
    pass


if userNum <100 or userNum > 200:
    print("Number is not between 100 and 200.")
else:
    pass

if not (userNum >= 0):
    print("Your number is negative.")
else:
    pass

#an if statement will check of the condition in not 0, or false, or None, or empty

if 7:
    print("This is true")
else:
    print("This is flase")
      #this will be true as long as number if not zero, not False, or the dring is empty ("")

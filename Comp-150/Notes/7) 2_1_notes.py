#Condational Statment
#   condition - one thing true one flase
#   consequent - something done when condition is true
#   alternative - when condition is false

# Comparison opoerator
#   greater than >
#   less than <
#   geater than or equal >=
#   less than or equal <=
#   equal ==
#   not equal !=

print (5<3)
print (5!=4)
print ("a"<"b")   #lexigraphical order
print ("a" == "A")
x=5
print (x==5)
print()


userNum = int(input("What is your number? "))
if userNum < 0:
    print("number it negative")
elif userNum == 0:
    print ("number is not positive or negative")
else:
    print("number is poitive")



usercode = input("Password please: ")
if usercode == "pretzel":
    print("you can enter")
else:
    print("Go away!")


#A(t) = P*e^(r*t)
import math

pricipal = float(input("What is your principle? "))
rate = float(input("What is your rate? "))
time = float(input("How many years you got? "))
save = float(input("How much do you want to save? "))

actualSavings = pricipal * math.exp(rate*time)

if actualSavings >= save:
    print ("You will meet your goal")
    print ("You have $" + str(actualSavings - save) +"above your goal.")
else:
    print ("You will not meet your goal")
    print ("You are $" + str(save - actualSavings) +"below your goal.")

#    print ("you are short by ${:.2f}".format(save - actualSavings))
#    or use "f strings"
#this is what you use to get rid of the .905486405865049860495 ect at the end










#while loop

#the cross between a for loop and if statement

#while condition:
#   run this unil this becomes false

while False:
    print("Not going to run")

for i in range (1, 6):
    print (i)

print()
i=1
while i <=5:
    print (i, end=" ")    #<------ little way to print everything on same line
    i=i+1
print()
print ("Loop is done")


userInput = input("Please enter 'yes': ")
while userInput != "yes":
    userInput = input("ENTER 'yes': ")
print("Thanks :)")

import datetime
year = datetime.datetime.now().year #<----- yets the current year
print (year)

#sentinal vale = a value that you wait for before continuing

userNum = -1
numstr = ""
while userNum !=0:
    userNum = int(input("Enter an intager (enter 0 to quit): "))
    numstr = numstr + str(userNum) + " "

print(numstr)



prod = 1
num = int(input("Enter an intager (0 to quit): "))

while num != 0:
    prod = prod * num
    num = int(input("Enter an intager (0 to quit): "))

print ("The product is", prod)







